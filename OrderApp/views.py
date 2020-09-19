from alipay import AliPay, AliPayConfig
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from CartApp.models import AxfCart
from CartApp.view_helper import get_total_price
from OrderApp.models import AxfOrder, AxfOrderGoods
from axf.settings import PRIVATE_KEY, PUBLIC_KEY


def orderDetail(request):
    orderid = request.GET.get('orderid')
    order = AxfOrder.objects.get(pk=orderid)
    context = {
        'order': order
    }

    return render(request, 'axf/order/order_detail.html', context=context)


def makeOrder(request):
    user_id = request.session.get('user_id')
    order = AxfOrder()
    order.o_user_id = user_id
    order.o_total_price = get_total_price(user_id)
    order.save()

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:
        ordergoods = AxfOrderGoods()
        ordergoods.og_order = order
        ordergoods.og_goods = cart.c_goods
        ordergoods.og_c_goods_num = cart.c_goods_num
        ordergoods.save()
        cart.delete()

    data = {
        'status': 200,
        'msg': 'ok',
        'orderid': order.id
    }
    return JsonResponse(data=data)


def testPay(request):
    alipay = AliPay(
        appid="2021000116673369",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False,  # 默认False
        config = AliPayConfig(timeout=15)  # 可选, 请求超时时间
    )

    subject = "AXF订单支付"
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="110",
        total_amount=10000,
        subject=subject,
        return_url="https://example.com",
        notify_url="https://example.com/notify" 
    )
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)
