from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins



class CategoryListView2(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)





class CategoryDetailView2(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def patch(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.delete(request,pk)



class CategoryListView1(APIView):
    def get(self,request):
        seria = CategorySerizlizer(instance=Category.objects.all(),many=True)
        return Response(seria.data,status=status.HTTP_200_OK)

    def post(self,request):
        seria = CategorySerizlizer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data,status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category,pk=cid))
        return Response(seria.data,status=status.HTTP_200_OK)
    def put(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category,pk=cid),data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_200_OK)
    def patch(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)
    def delete(self,request,cid):
        get_object_or_404(Category,pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def categoryList(request):
    if request.method == "GET":
        seria = CategorySerizlizer(instance=Category.objects.all(),many=True)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        seria = CategorySerizlizer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def categoryDetail(request,cid):
    model = get_object_or_404(Category,pk=cid)
    if request.method == "GET":
        seria = CategorySerizlizer(instance=model)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        seria = CategorySerizlizer(instance=model,data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许"+request.method+"操作")


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer


class CategoryViewSets2(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer



class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

class GoodViewsSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer


class GoodImgsViewsSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer