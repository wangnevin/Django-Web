from django.urls import path, include
from .views import *

urlpatterns = [
    path('login.html', userLogin, name='userLogin'),
]
