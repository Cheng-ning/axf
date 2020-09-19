from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfOrder(models.Model):
    o_user = models.ForeignKey(AxfUser)
    o_time = models.DateTimeField(auto_now_add=True)
    o_total_price = models.FloatField()
    class Meta:
        db_table = 'axf_order'


class AxfOrderGoods(models.Model):
    og_order = models.ForeignKey(AxfOrder)
    og_goods = models.ForeignKey(AxfGoods)
    og_c_goods_num = models.IntegerField()
    class Meta:
        db_table = 'axf_orderGoods'