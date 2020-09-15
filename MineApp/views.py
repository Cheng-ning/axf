from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from UserApp.models import AxfUser


def mine(request):
    uid = request.session.get('user_id')
    if uid:
        user = AxfUser.objects.get(pk=uid)
        return render(request, 'axf/main/mine/mine.html', {'user1': user})

    else:
        return render(request, 'axf/main/mine/mine.html')


def logout(request):
    if request.session['user_id']:
        request.session.flush()
    return redirect(reverse('axfmine:mine'))