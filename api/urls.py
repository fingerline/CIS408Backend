from django.urls import path
from . import views
from rest_framework import routers, serializers, viewsets



urlpatterns=[
  path('', views.class_list),
  path('<int:id>', views.class_detail)
]