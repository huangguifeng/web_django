from django.contrib import admin
from .models import  *
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle','gpic','gprice','gunit','gclick','gjianjie','gkuncun','gcontent','gtype','isDelete']
    list_per_page = 20


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['ttitle','isDelete']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)