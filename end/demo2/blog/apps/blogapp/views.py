from django.shortcuts import render,redirect
from django.http import HttpResponse
# django自带了分页与分页器
from django.core.paginator import Page,Paginator
# 一个Page中有object_list代表当前页的所有对象
# has_next 是不是有下一页

from .models import *
# Create your views here.
def index(request):

    ads = Ads.objects.all()
    articles = Article.objects.all()
    # locals可以返回作用域局部变量
    paginator = Paginator(articles,2)
    num = request.GET.get("pagenum",1)
    page = paginator.get_page(num)
    return render(request,'index.html',{"ads":ads,"page":page})
    # return HttpResponse("首页")

def detail(request,articleid):
    return render(request,'single.html')
    # return HttpResponse("文章"+articleid)

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("联系我们")


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")







