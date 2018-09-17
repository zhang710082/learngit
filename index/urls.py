from django.conf.urls import url
from .views import *
urlpatterns = [
    #访问路径是 /
    url(r'^$',index_views),
    #访问路径是 /login
    url(r'^login/$',login_views),
    #访问路径是 /register
    url(r'^register/$',register_views),
    url(r'^phone/$',phone_views),
    url(r'^01login/$',login01_views),
    url(r'^logout/$',logout_views),
    url(r'^goods/$',goods_views),
    url(r'^cartinfo/$',cartinfo_views),
    url(r'^cart_count',cart_count_views),
    url(r'^findtext/$',find_views),
]







