from django.db import models
from accounts.models import MyUser


# Create your models here.
class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')
    credit = models.IntegerField('学分', default=0)
