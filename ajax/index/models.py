from django.db import models

# Create your models here.
class Register(models.Model):
    uname = models.CharField(max_length=30,verbose_name='用户名')
    upwd = models.CharField(max_length=15,verbose_name='密码')
    uphone = models.CharField(max_length=11,verbose_name='电话号码')
    uemail = models.EmailField(verbose_name='邮箱')
    def __str__(self):
        return self.uname
    def to_dict(self):
        dic = {
            "uname":self.uname,
            "upwd":self.upwd,
            "uphone":self.uphone,
            "uemail":self.uemail
        }
        return dic
class Province(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class City(models.Model):
    name = models.CharField(max_length=20)
    property = models.ForeignKey(Province)
    def __str__(self):
        return self.name
