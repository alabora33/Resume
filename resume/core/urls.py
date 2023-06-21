from django.urls import path
from .views import index

urlpatterns =[
    path('my_profile', index, name='index'),
]