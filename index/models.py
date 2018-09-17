from django.db import models

# Create your models here.
class User(models.Model):
    uphone = models.CharField(max_length=20,verbose_name='电话')
    upwd = models.CharField(max_length=20,verbose_name='密码')
    uemail = models.EmailField(verbose_name='邮箱')
    uname = models.CharField(max_length=20,verbose_name='用户名')
    isActive = models.BooleanField(default=True,verbose_name='激活')
    def __str__(self):
        return self.uname
    def to_dict(self):
        dic = {
            "uname":self.uname,
            "upwd":self.upwd,
            "uemail":self.uemail,
            "uphone":self.uphone,
            'id':self.id
        }
        return dic
class GoodsType(models.Model):
    title = models.CharField(max_length=50,verbose_name='类型名称')
    picture = models.ImageField(upload_to='static/upload/goodstype',verbose_name='商品类型图片',null=True)
    desc = models.TextField(verbose_name='商品类型描述')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'GoodsType'
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name
    def to_dict(self):
        dic = {
            'title':self.title,
            'picture':self.picture.__str__(),
            'desc':self.desc
        }
        return dic
class Goods(models.Model):
    title = models.CharField(max_length=30,verbose_name='商品名称')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
    spec = models.CharField(max_length=30,verbose_name='规格')
    picture = models.ImageField(upload_to='static/upload/goods',verbose_name='商品图片',null=True)
    goodsType = models.ForeignKey(GoodsType,verbose_name='商品类型')
    isActive = models.BooleanField(default=True,verbose_name='是否上架')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
class CartInfo(models.Model):
    user = models.ForeignKey(User,verbose_name='用户',db_column='user_id')
    goods = models.ForeignKey(Goods,verbose_name='商品名称',db_column='goods_id')
    count = models.IntegerField(verbose_name='购买数量')
    def __str__(self):
        return self.count
    class Meta:
        db_table = 'cartinfo'
        verbose_name = "购物车"
        verbose_name_plural = verbose_name