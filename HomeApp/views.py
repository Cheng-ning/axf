from django.shortcuts import render

# Create your views here.
from HomeApp.models import Wheel


def home(request):
    wheels = Wheel.objects.all()

    return render(request, 'axf/main/home/home.html', locals())