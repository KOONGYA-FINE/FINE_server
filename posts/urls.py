from django.urls import path
from posts.views import *

urlpatterns = [
    path("", PostList.as_view()),
    path("<int:postid>/", PostDetail.as_view()),
    path("<int:postid>/<int:userid>", SavePost.as_view()),
]
