from django.urls import path
from . import views

urlpatterns = [
    path('post-upvotes/', views.PostUpvoteList.as_view())
]
