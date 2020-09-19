from CartApp.models import AxfCart


def get_total_price(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total_price = 0

    for cart in carts:
        total_price += cart.c_goods_num * cart.c_goods.price

    return '{:.2f}'.format(total_price)