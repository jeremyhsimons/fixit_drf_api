from django.urls import path
from . import views

urlpatterns = [
    path('post-upvotes/', views.PostUpvoteList.as_view()),
    path('post-upvotes/<int:pk>/', views.PostUpvoteDetail.as_view()),
]
