from django.shortcuts import render
from django.shortcuts import get_object_or_404

# models
from .models import Post, Post_KR

# serializer
from .serializers import PostSerializer, Post_KRSerializer

# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# PostList(전체)
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PostDetail(특정 값)
class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
