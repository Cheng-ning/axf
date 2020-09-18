import uuid
from smtplib import SMTPRecipientsRefused

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password,check_password
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from six import BytesIO

from UserApp.models import AxfUser
from UserApp.view_helper import sendEmail
from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        icon = request.FILES.get('icon')

        password = make_password(password)

        user = AxfUser()
        user.username = username
        user.password = password
        user.email = email
        user.icon = icon
        token = uuid.uuid4()
        user.token = token


        try:
            sendEmail(username, email, token)
        except SMTPRecipientsRefused:
            return HttpResponse('邮箱不存在')

        cache.set(token, user.id, timeout=60)
        user.save()

        return redirect(reverse('axfuser:login'))



def login(request):
    if request.method == 'POST':
        imgcode = request.POST.get('imgCode')
        verify_code = request.session.get('verify_code')
        if imgcode.upper() == verify_code.upper():
            username = request.POST.get('username')
            users = AxfUser.objects.filter(username=username)
            request.session.flush()
            if users.exists():
                user = users[0]
                password = request.POST.get('password')
                if check_password(password, user.password):
                    if user.active:
                        request.session['user_id'] = user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        return render(request, 'axf/user/login/login.html', {'msg': '账户未激活'})
                else:
                    return render(request, 'axf/user/login/login.html', {'msg': '用户名或密码错误'})

            else:
                return render(request, 'axf/user/login/login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'axf/user/login/login.html', {'msg': '验证码错误'})
    else:
        return render(request, 'axf/user/login/login.html')


def checkName(request):
    data = {
        'status': 200,
        'message': '用户名可以使用'
    }
    username = request.GET.get('username')
    user = AxfUser.objects.filter(username=username)
    if user.exists():
        data['status'] = 201
        data['message'] = '用户名已存在'
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def checkCode(request):
    data = {
        'status': 201,
        'msg': '验证码错误'
    }
    verify_code = request.session.get('verify_code')
    imgcode = request.GET.get('imgcode')
    if verify_code.upper() == imgcode.upper():
        data['status'] = 200
        data['msg'] = ''
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)



def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)
    # FONT_PATH 验证码的字体
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(1000):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def account(request):
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.active = True
        user.save()
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送')