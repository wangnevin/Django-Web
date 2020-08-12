from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<int:page>', assign, name='assign'),
    path('info_edit', info_edit, name='info_edit'),
    path('assign_submit', assign_submit, name='assign_submit'),
    path('assign_edit/<int:assign_id>', assign_edit, name='assign_edit')
]
