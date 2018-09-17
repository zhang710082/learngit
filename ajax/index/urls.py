from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^01_xmlhttp/$',xml_views),
    url(r'^02_get/$',get01_views),
    url(r'^02_server/$',server02_views),
    url(r'^03_textajax/$',text_views),
    url(r'^03_gettext/$',gettext_views),
    url(r'^04_post',post04_views),
    url(r'^04_server/$',server04_views),
    url(r'^05_post/$',post06_views),
    url(r'^05_server/$',server06_views),
    url(r'^07_register/$',register_views),
    url(r'^07_server/$',server07_views),
    url(r'^08_json/$',json_views),
    url(r'^08_server/$',server08_views),
    url(r'^09_jqload/$',jqload_views),
    url(r'^09_server/$',server09_views),
    url(r'^10_jqget/$',jqget_views),
    url(r'^10_server/$',server10_views),
    url(r'^11_server/$',server11_views),
    url(r'^12_jqajax/$',jqajax_views),
    url(r'^12_server/$',server12_views),
    url(r'^13_server/$',server13_views),
    url(r'^14_jqajax/$',jqajax14_views),
    url(r'^14_server/$',server14_views),

]