from django.contrib import admin
from .models import *
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id',"gtitle",'gprice','gjianjie',
                    'isDelete','gunit',"gkuncun",'gclick',
                    'gtype']
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle','isDelete']

admin.site.register(GoodsInfo,GoodsInfoAdmin)
admin.site.register(TypeInfo,TypeInfoAdmin)