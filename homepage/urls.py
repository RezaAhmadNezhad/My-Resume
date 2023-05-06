from django.urls import path
from homepage.views import *

appname = 'homepage'

urlpatterns = [
    path ('', index, name= 'index'),
]