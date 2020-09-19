from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^orderDetail/', views.orderDetail),

    url(r'^makeorder/', views.makeOrder),

    url(r'^testPay/', views.testPay)
]