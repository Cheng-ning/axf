from django.conf.urls import url

from CartApp import views

urlpatterns=[
    url(r'^cart/', views.cart, name='cart'),

    # 添加到购物车
    url(r'^addToCart/', views.addToCart),

    url(r'^subCart/', views.subCart),

    url(r'^addCart/', views.addCart),

    url(r'^subToCart/', views.subToCart),

    url(r'^changeStatus/', views.changeStatus),

    url(r'^allSelect/', views.all_Select)
]