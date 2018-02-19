from django.shortcuts import render
from post.models import Post
from post.serializers import PostDetailSerializer
from django.db.models import Q
from search.serializers import (SearchSerializer,
                                )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.

class SearchAPIView(APIView):
    serializer_class = SearchSerializer

    def post(self,request, *args, **kwargs):
        search_text = request.data["search_text"]
        if search_text:
            search_queryset = Post.objects.filter(
                Q(title__icontains=search_text)|
                Q(user__fullname__icontains=search_text)|
                Q(url__icontains=search_text)|
                Q(description__icontains=search_text)
            )
            if search_queryset:
                serializer = PostDetailSerializer(search_queryset, many=True)
                result_data = serializer.data
                response_data = {'search_result':result_data}
                return Response(response_data,status=HTTP_200_OK)
            else:
                return Response({'msg':'There is no content with the search_word'}, status=HTTP_200_OK)
        else:
            return Response({'msg':'There is no search_text'}, status=HTTP_400_BAD_REQUEST)