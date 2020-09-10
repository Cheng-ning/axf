from django.shortcuts import render

# Create your views here.
def market(request):
    path = request.path
    return render(request, 'axf/main/market/market.html', locals())