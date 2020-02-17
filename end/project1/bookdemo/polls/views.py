from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("首页")

def detail(request,qid):
    return HttpResponse("详情页"+qid)


def result(request,qid):
    return HttpResponse("结果页"+qid)

