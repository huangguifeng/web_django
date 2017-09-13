#coding=utf-8
from django.db import models

# Create your models here.

class CartInfo(models.Model):
    # 用户
    user = models.ForeignKey('tt_user.UserInfo')
    # 商品
    goods = models.ForeignKey('tt_goods.GoodsInfo')
    # 数量
    count = models.IntegerField()