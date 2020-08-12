from django.db import models


# Create your models here.
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField('角色', max_length=10, default='暂无信息')

    def __str__(self):
        return self.role
