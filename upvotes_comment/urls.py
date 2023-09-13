from django.urls import path
from . import views

urlpatterns = [
    path('comment-upvotes/', views.CommentUpvoteList.as_view()),
]
