from django.db import models


# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField('科目', max_length=50, default='暂无信息')

    def __str__(self):
        return self.type
