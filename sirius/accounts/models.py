from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from role.models import Role


class MyUser(AbstractUser):
    name = models.CharField('姓名', max_length=50, default='匿名用户')
    class_number = models.CharField('班级', max_length=50, default='暂无信息')
    grade = models.CharField('年级', max_length=10, default='暂无信息')
    address = models.CharField('住址', max_length=100, default='暂无信息')
    telephone = models.CharField('电话', max_length=11, default='暂无信息')
    wx = models.CharField('微信', max_length=50, default='暂无信息')
    qq = models.CharField('QQ', max_length=50, default='暂无信息')
    wb = models.CharField('微博', max_length=100, default='暂无信息')
    photo = models.ImageField('头像', blank=True, upload_to='images/user/')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='角色', default=2)

    def __str__(self):
        return self.name
