from django.db import models

# Create your models here.

class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'




class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=64)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)
    isxf = models.BooleanField(default=False)

    # 排序规则
    pmdesc = models.IntegerField()
    # 商品的详情
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()
    # 类别的id
    categoryid = models.IntegerField()
    # 子类别的id  二级联动 三级联动
    childcid = models.IntegerField()


    childcidname = models.CharField(max_length=128)
    # 商家id
    dealerid = models.IntegerField()
    # 商店的储备数量
    storenums = models.IntegerField()
    # 商品的数据
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'