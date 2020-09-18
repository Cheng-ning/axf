from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart
from CartApp.view_helper import get_total_price
from MarketApp.models import AxfGoods


def cart(request):
    u_id = request.session.get('user_id')
    if u_id:
        carts = AxfCart.objects.filter(c_user_id=u_id)
        is_all_select = not carts.filter(c_is_select=False).exists()
        total_price = get_total_price(u_id)

        context = {
            'carts': carts,
            'is_all_select': is_all_select,
            'total_price': total_price
        }

        return render(request, 'axf/main/cart/cart.html', context=context)
    else:
        return redirect(reverse('axfuser:login'))


def addToCart(request):
    g_id = request.GET.get('g_id')
    u_id = request.session.get('user_id')
    carts = AxfCart.objects.filter(c_goods_id=g_id).filter(c_user_id=u_id)

    if carts.count() == 0:
        cart = AxfCart()
        cart.c_user_id = u_id
        cart.c_goods_id = g_id
    else:
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num + 1
    cart.save()

    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num
    }
    return JsonResponse(data=data)


def subCart(request):
    g_id = request.GET.get('g_id')
    u_id = request.session.get('user_id')
    carts = AxfCart.objects.filter(c_goods_id=g_id).filter(c_user_id=u_id)
    cart = carts.first()

    if cart.c_goods_num > 0:
        cart.c_goods_num -= 1
        cart.save()
    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num,
    }
    return JsonResponse(data=data)



@csrf_exempt
def addCart(request):
    cart_id = request.POST.get('cart_id')
    cart = AxfCart.objects.get(pk=cart_id)
    cart.c_goods_num += 1
    cart.save()
    user_id = request.session.get('user_id')
    total_price = get_total_price(user_id)

    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num,
        'total_price': total_price
    }
    return JsonResponse(data=data)

@csrf_exempt
def subToCart(request):
    cart_id = request.POST.get('cart_id')
    cart = AxfCart.objects.get(pk=cart_id)
    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num
    }

    if cart.c_goods_num > 1:
        cart.c_goods_num -= 1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    else:
        cart.delete()
        data['c_goods_num'] = 0

    user_id = request.session.get('user_id')
    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)



@csrf_exempt
def changeStatus(request):
    cartid = request.POST.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)
    cart.c_is_select = not cart.c_is_select
    cart.save()

    user_id = request.session.get('user_id')
    total_price = get_total_price(user_id)
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()
    data = {
        'status': 200,
        'msg': 'ok',
        'c_is_select': cart.c_is_select,
        'is_all_select': is_all_select,
        'total_price': total_price
    }
    return JsonResponse(data=data)


def all_Select(request):
    cartid_list = request.GET.get('cartid_list')
    id_list = cartid_list.split('#')
    cart_list = AxfCart.objects.filter(id__in=id_list)
    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    u_id = request.session.get('user_id')
    total_price = get_total_price(u_id)
    data = {
        'status': 200,
        'msg': 'ok',
        'total_price': total_price
    }
    return JsonResponse(data=data)


