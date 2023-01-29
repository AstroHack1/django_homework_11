from django.urls import path,re_path
from .views import begin_numbers,begin_uppercase_letters

urlpatterns = [
    re_path(r'^\d+',begin_numbers,name='begin_numbers'),
    re_path(r'^[A-Z]+',begin_uppercase_letters,name='begin_uppercase_letters'),
]