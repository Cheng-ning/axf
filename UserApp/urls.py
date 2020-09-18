from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),

    url(r'^login/', views.login, name='login'),

    url(r'^checkname/', views.checkName, name='checkname'),

    url(r'^get_code/', views.get_code, name='get_code'),

    url(r'^checkcode/', views.checkCode, name='checkcode'),
    # #发送邮件
    # url(r'^sendemail', views.sendemail(), name='sendemail')

    #激活
    url(r'^account', views.account, name='account')

]