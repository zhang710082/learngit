/**
 * Created by tarena on 18-9-3.
 */
function func() {
    if(window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
        window.alert('创建的XMLHttpRequest')
    }else{
        var xhr = new ActiveXObject('Microsoft.XMLHTTP');
        window.alert('创建的ActiveXObject')
    }
}
function createxhr(){
     if(window.XMLHttpRequest){
        return new XMLHttpRequest();
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP');
    }
}