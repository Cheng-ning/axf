from django.shortcuts import render

# Create your views here.
from HomeApp.models import Wheel, Nav, Mustbuy, Mainshow


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    mainshows = Mainshow.objects.all()

    return render(request, 'axf/main/home/home.html', locals())