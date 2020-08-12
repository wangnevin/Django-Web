from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/<int:page1>/<int:page2>', review, name='review'),
    path('assign_review/<int:assign_id>', assign_review, name='assign_review'),
    path('download/<int:assign_id>', assign_download, name='assign_download'),
]
