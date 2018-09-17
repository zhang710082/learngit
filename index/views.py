from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import json

# Create your views here.
def index_views(request):
    return render(request,'index.html')

# /login 对应的视图
def login_views(request):
    if request.method == "GET":
        s = request.session.get('uid',False)
        if s:
            return redirect('/')
        else:
            if request.COOKIES.get('uid',False):
                id = request.COOKIES['uid']
                uphone = request.COOKIES['uphone']
                request.session['uid'] = id
                request.session['uphone'] = uphone
                return redirect('/')
            form = LoginForm()
            return render(request,'login.html',locals())
    uphone = request.POST.get('uphone',None)
    obj = User.objects.filter(uphone=uphone)
    if obj:
        if obj[0].upwd == request.POST.get('upwd',False):
            request.session['uid'] = obj[0].id
            request.session['uphone'] = uphone
            if 'isSaved' in request.POST:
                resp = redirect('/')
                resp.set_cookie('uid',obj[0].id,60*60*24)
                resp.set_cookie('uphone',uphone,60*60*24)
                return resp
            return redirect('/')
        err = '密码不正确'
        form = LoginForm()
        return render(request, 'login.html', locals())
    err = '用户名不正确'
    form = LoginForm()
    return render(request, 'login.html', locals())
# /register 对应的视图
def register_views(request):
    if request.method =="GET":
        return render(request,'register.html')
    dic = {
        'uname':request.POST.get('uname',None),
        'upwd':request.POST.get('upwd',None),
        'uphone':request.POST.get('uphone',None),
        'uemail':request.POST.get('uemail',None)
    }
    User(**dic).save()
    u = User.objects.get(uphone=request.POST.get('uphone',None))
    request.session['uid'] = u.id
    request.session['uphone'] = u.uphone

    return redirect('/')
def phone_views(request):
    uphone = request.GET.get('uphone',None)
    obj = User.objects.filter(uphone=uphone)
    if obj:
        return HttpResponse("用户名已存在")
    else:
        return HttpResponse("OK")
def login01_views(request):
    if request.session.get('uid',False):
        id = request.session['uid']
        obj = User.objects.get(id=id)
        return HttpResponse(json.dumps(obj.to_dict()))
    else:
        if request.COOKIES.get('uid', False):
            request.session['uid'] = request.COOKIES['uid']
            request.session['uphone'] = request.COOKIES['uphone']
            id = request.COOKIES['uid']
            obj = User.objects.get(id=id)
            return HttpResponse(json.dumps(obj.to_dict()))
        else:
            return HttpResponse("NO")
def logout_views(request):
    url = request.META.get('HTTP_REFERER','/')
    resp = redirect(url)
    if request.session.get('uid',False):
        del request.session['uid']
        del request.session['uphone']
    if request.COOKIES.get('uid',False):
        resp.delete_cookie('uid')
        resp.delete_cookie('uphone')
    return resp
def goods_views(request):
    l = []
    goodstypes = GoodsType.objects.all()
    for goodstype in goodstypes:
        dic = {}
        goods = goodstype.goods_set.all()
        goods = serializers.serialize('json',goods)
        goodstype = json.dumps(goodstype.to_dict())
        dic['type'] = goodstype
        dic['goods'] = goods
        l.append(dic)
    return HttpResponse(json.dumps(l))
def cartinfo_views(request):
    goods_id = request.GET.get('goods_id',None)
    user_id = request.session.get('uid',None)
    obj = CartInfo.objects.filter(goods_id=goods_id,user_id=user_id)
    if obj:
        s = int(obj[0].count)
        obj[0].count = s + 1
        obj[0].save()
        return HttpResponse('更新成功')
    else:
        dic = {
            "count":1,
            "goods_id":goods_id,
            "user_id":user_id
        }
        CartInfo(**dic).save()
        return HttpResponse('购买成功')
def cart_count_views(request):
    if 'uid' not in request.session:
        dic = {
            'count':0
        }
        return HttpResponse(json.dumps(dic))
    else:
        uid = request.session['uid']
        all_cart = CartInfo.objects.filter(user_id=uid)
        total_count = 0
        for cart in all_cart:
            total_count += cart.count
        dic = {
            'count':total_count
        }
        return HttpResponse(json.dumps(dic))

def find_views(request):
    obj = Goods.objects.get(id=1)
    obj = json.loads(obj)
    print(obj)
