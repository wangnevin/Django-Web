from django.db import models
from django.utils import timezone
from accounts.models import MyUser
from type.models import Type


# Create your models here.
class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=50, default='作业')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='科目')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')
    content = models.FileField('作业', upload_to='assign/')
    created = models.DateTimeField('创建时间', default=timezone.now)
    updated = models.DateTimeField('更新时间', auto_now=True)
    is_reviewed = models.BooleanField('批改', max_length=10, default=False)
    score = models.IntegerField('得分', default=0)
    credit = models.IntegerField('获得学分', default=0)

    def __str__(self):
        return self.title
