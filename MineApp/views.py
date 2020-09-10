from django.shortcuts import render

# Create your views here.
def mine(request):
    path = request.path
    return render(request, 'axf/main/mine/mine.html', locals())
