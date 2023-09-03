from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

class BlogListView(APIView):
    def get(self,request,*args, **kwargs):

        post=Post.postobject.all()[0:5]
        serializer=PostSerializer(post,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BlogDetaillView(APIView):
    def get(self,request,post_slug,*args, **kwargs):
        data1= Post.objects.filter(slug=post_slug).first()
        serializer=PostSerializer(data1)
        if data1:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

