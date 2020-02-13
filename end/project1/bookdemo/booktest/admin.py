from django.contrib import admin
#定义后端显示界面
from django.contrib.admin import ModelAdmin
# Register your models here.
# django 自带的后台管理操作需要在此处实现


#注册自己需要管理的模型 Book Hero
from .models import Book,Hero


class HeroInline(admin.StackedInline):
    # 关联类
    model = Hero
    extra = 2

class HeroAdmin(ModelAdmin):
    list_display = ('name','gender','content','book')

admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    list_display = ('title','price',"pub_data")

admin.site.register(Book,BookAdmin)



