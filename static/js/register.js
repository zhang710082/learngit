/**
 * Created by tarena on 18-9-5.
 */


flag = true
function checkUphone(){
    var value = $("[name='uphone']").val();
    if(value.trim().length == 11){
        $('#phone').load('/phone/','uphone='+value,function(resText){
            if(resText =='用户名已存在'){
                $('#phone').html('手机号已存在');
                flag = false
            }else{
                $('#phone').html('通过');
                flag = true
            }
            })
    }else{
        $('#phone').html('手机号码位数不正确');
        flag = false
    }

}
function checkUpwd(){
    var pwd = $("[name='upwd']").val().trim();
    console.log(pwd.length);
    if(pwd.length<=6){
        $('#pwd').html("密码输入有误");
        return false
    }else{
        $('#pwd').html("通过");
        return true
    }
}
function checkAgpwd(){
    var cpwd = $("#cpwd").val();
    if(cpwd == $("[name='upwd']").val()){
        $('#agpwd').html("通过");
        return true
    }else{
        $('#agpwd').html("密码不一致");
        return false
    }
}
function checkEmail(){
    var email = $("[name='uemail']").val().trim();
    if(email){
        $("#email").html("通过");
        return true
    }else{
        $("#email").html("邮箱输入有误");
        return false
    }
}
function checkUname(){
    var name = $("[name='uname']").val().trim();
    if(name){
        $('#name').html("通过");
        return true
    }else{
        $('#name').html("用户名输入有误");
        return false
    }
}
$(function(){
    $("[name='uphone']").blur(function(){
        checkUphone()
    });
    $("[name='upwd']").blur(function(){
        checkUpwd()
    });
    $('#cpwd').blur(function(){
        checkAgpwd()
    });
    $("[name='uemail']").blur(function(){
        checkEmail()
    });
    $("[name='uname']").blur(function(){
        checkUname()
    });
    $("#submit").submit(function(){
        checkUphone()
        if(flag&&checkUpwd()&&checkAgpwd()&&checkEmail()&&checkUname()){
            return true
        }else{
            $('#s').html("信息输入有误");
            return false
        }
    })
});
