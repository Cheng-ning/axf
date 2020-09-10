from django.shortcuts import render

# Create your views here.

def cart(request):
    path = request.path
    return render(request, 'axf/main/cart/cart.html', locals())