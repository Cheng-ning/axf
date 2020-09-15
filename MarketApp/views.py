from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):
    foodtypes = AxfFoodType.objects.all()
    typeid = request.GET.get('typeid', '104749')
    childtypenames = AxfFoodType.objects.get(typeid=typeid).childtypenames
    childtypename_list = childtypenames.split('#')
    child_list = []

    for childtypename in childtypename_list:
        child = childtypename.split(':')
        child_list.append(child)

    goods_list = AxfGoods.objects.filter(categoryid=typeid)
    childcid = request.GET.get('childcid', '0')

    if childcid == '0':
        goods_list = goods_list
    else:
        goods_list = goods_list.filter(childcid=childcid)

    sort_rule_list = [
        ['综合排序', '0'],
        ['价格升序', 'price_up'],
        ['价格降序', 'price_down'],
        ['销量升序', 'product_up'],
        ['销量降序', 'product_down']
    ]
    sort_rule = request.GET.get('sort', '0')

    if sort_rule == '0':
        pass
    elif sort_rule == 'price_up':
        goods_list = goods_list.order_by('price')
    elif sort_rule == 'price_down':
        goods_list = goods_list.order_by('-price')
    elif sort_rule == 'product_up':
        goods_list = goods_list.order_by('productnum')
    elif sort_rule == 'product_down':
        goods_list = goods_list.order_by('-productnum')

    context = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'childcid': childcid,
        'child_list': child_list,
        'sort_rule_list': sort_rule_list,
        'rule': sort_rule
    }

    return render(request, 'axf/main/market/market.html', context= context)