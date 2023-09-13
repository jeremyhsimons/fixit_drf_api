from django.urls import path
from . import views

urlpatterns = [
    path('stars/', views.StarList.as_view()),
]
