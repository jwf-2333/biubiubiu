from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name="图书名")
    price = models.FloatField(default=0)
    pub_data = models.DateField(default="1983-06-01")
    desc = models.CharField(max_length=50,null=True,blank=True,db_column='description',help_text="请输入书籍备注信息")


    def __str__(self):
        return  self.title

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)

    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='heros')
    def __str__(self):
        return  self.name

class UserManager(models.Manager):
    def deleteByTelePhone(self,tele):
        user = self.get(telephone=tele)
        user.delete()


class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    objects = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        db_table = "用户类"
        ordering = ["id"]
        verbose_name = "用户模型类"
        verbose_name_plural = "用户模型类"



class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True,verbose_name="注册日期")
    # concact = models.OneToOneField('Concact',on_delete=models.CASCADE)

class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="875016526@qq.com")
    account = models.OneToOneField(Account,on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")

class Tag(models.Model):
    name = models.CharField(max_length=10,verbose_name="标签名")
    article = models.ManyToManyField(Article)



# 一对多   一方book   实例b   多方hero  实例h
# 一找多   b.hero_set.all()  如果定义过related_name='hero' 则使用 b.heros.all()
# 多找一   h.book

# 一对一   一方account   实例a    一方concact 实例c
#  a找c  a.concact
#  c找a  c.account


# 多对多  多方Article  实例a   多方Tag  实例t   关系字段可以定义在任意一方
#  添加关系 t.article.add(a)    移除关系  t.article.remove(a)
#  a找所有的t   a.tag_set.all()  如果定义过related_name= 'tags' 则使用a.tags.all()
#  t找所有的a   t.article.all()