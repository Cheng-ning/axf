from django.shortcuts import render

# Create your views here.
def home(request):
    path = request.path
    print(path)
    return render(request, 'axf/main/home/home.html', locals())