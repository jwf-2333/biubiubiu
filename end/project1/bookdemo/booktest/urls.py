from django.conf.urls import url
from . import views

app_name = "booktest"
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'detail/(\d+)/$',views.detail,name='detail'),
    url(r'^about/$',views.about,name='about'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^edithhero/(\d+)/$', views.edithhero, name='edithhero'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^edithbook/(\d+)/$',views.edithbook,name='edithbook'),
]