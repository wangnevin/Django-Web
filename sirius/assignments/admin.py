from django.contrib import admin
from .models import *

admin.site.site_title = '作业管理后台'
admin.site.site_header = '作业管理'


# Register your models here.
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'user', 'content', 'created', 'updated', 'is_reviewed', 'score', 'credit']
