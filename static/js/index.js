/**
 * Created by tarena on 18-9-6.
 */

function check_login(){
    $.get('/01login/',function(data){
       if(data !=="NO"){
           console.log(data);
           $('#i1').text("欢迎"+data.uname);
           $('#i2').text('退出');
           $('#i2').attr('href','/logout/')
       }
    },'json')
}
function loadGoods(){
    $.get('/goods/',function(data){
        var html = '';
        $.each(data,function(i,obj){
            html+="<div class='item'>";
            var type = JSON.parse(obj.type);
            html+="<p class='title'>";
            html+="<a href='#'>更多</a>";
            html+="<img src=/"+type.picture+">";
            html+="</p>";
            html+="<ul>";
            var goods = JSON.parse((obj.goods));
            $.each(goods,function(i,obj){
                console.log(obj)
                html+="<li ";
                if((i+1) % 5 == 0){
                    html+="class='no-margin'"
                }
                html+=">";
                html+="<p>";
                html+="<img src=/"+obj.fields.picture+">";
                html+="</p>";
                html+="<div class='content'>";
                html+="<a href='javascript:cart("+obj.pk+")' class='cart'>";
                html+='<img src="/static/images/cart.png">'
                html+="</a>";
                html+="<p>"+obj.fields.title+"</p>";
                html+="<span>"+"&yen"+obj.fields.price+"/"+obj.fields.spec+"</span>";
                html+="</div>";
                html+="</li>";
            });
            html+="</ul>";
            html+="</div>";
        });
        $('#main').html(html)
    },'json')
}

function cart(goods_id){
    $.get('/01login/',function(data){
       if(data == "NO"){
           alert('请登录')
       }else{
           url = '/cartinfo/?goods_id='+goods_id
           $.get(url,function(data){
               load_count()
               alert(data)
           },'text')
       }
    },'text')}

function load_count(){
    $.get('/cart_count/',function(data){
        $('#mycart>a').html('我的购物车('+data.count+")")
    },'json')
}







$(function(){
    check_login()
    loadGoods()
    load_count()
})











































