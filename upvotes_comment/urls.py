from django.urls import path
from . import views

urlpatterns = [
    path('comment-upvotes/', views.CommentUpvoteList.as_view()),
    path('comment-upvotes/<int:pk>/', views.CommentUpvoteDetail.as_view())
]
