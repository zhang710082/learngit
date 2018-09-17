from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json
# Create your views here.
def xml_views(request):
    return render(request,'01.html')
def get01_views(request):
    return render(request,'02.html')
def server02_views(request):
    return HttpResponse('这是服务器端响应回去的数据')
def text_views(request):
    return render(request,'03.html')
def gettext_views(request):
    value = request.GET.get('value',None)
    return HttpResponse('欢迎'+value)
def post04_views(request):
    return render(request,'04.html')
def server04_views(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse('用户名：'+uname+'密码:'+upwd)
def post06_views(request):
    return render(request,'05.html')
def server06_views(request):
    uname = request.POST.get('uname',None)
    return HttpResponse('欢迎'+uname)
def register_views(request):
    return render(request,'06.html')
def server07_views(request):
    uname = request.POST.get('uname',None)
    l = Register.objects.filter(uname=uname)
    if l:
        return HttpResponse('用户名已存在')
    return HttpResponse('通过')
def json_views(request):
    return render(request,'07.html')
def server08_views(request):
    l = ['小张','小李']
    dic = {
        "1":2,
        "2":3,
        "3":4
    }
    l = [
        {
            "name":"小张",
            "age":20,
            "gender":"男"
        },
        {
            "name":"小李",
            "age":25,
            "gender":"男"
        }
    ]
    user = Register.objects.all()
    # user = Register.objects.get(uname='小张')
    # dic = user.to_dict()
    user = serializers.serialize('json',user)
    return HttpResponse(user)
def jqload_views(request):
    return render(request,'08.html')
def server09_views(request):
    uname = request.GET.get('uname',None)
    uage = request.GET.get('uage',None)
    return HttpResponse(uname+uage)
    return HttpResponse("使用jquery的load发送的请求")
def jqget_views(request):
    return render(request,'09.html')

def server10_views(request):
    print(request.GET.get('name',None))
    print(request.GET.get('age',None))
    return HttpResponse('<h1>这是get方法发送的异步请求</h1>')
def server11_views(request):
    return HttpResponse('这是post请求的响应')
def jqajax_views(request):
    return render(request,'10.html')
def server12_views(request):
    l = Province.objects.all()
    return HttpResponse(serializers.serialize('json',l))
def server13_views(request):
    id = request.GET.get("id",None)
    obj = City.objects.filter(property_id=id)
    return HttpResponse(serializers.serialize('json',obj))
def jqajax14_views(request):
    return render(request,'11.html')
def server14_views(request):
    value = request.POST.get('value',None)
    return HttpResponse(value)