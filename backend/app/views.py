from django import forms
from django.shortcuts import render
from rest_framework import filters, generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer

from .models import APIKey, Video, VideoThumbNail
from .serializers import APIKeySerializer, VideoSerializer, VideoThumbNailSerializer


class GetVideosPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10


class GetVideos(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = VideoSerializer
    pagination_class = GetVideosPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')

    def get_queryset(self):
        api_keys = APIKey.objects.filter(is_limit_over=False)
        if not len(api_keys):
            raise forms.ValidationError("All APIKey's Quota is over, Add a new APIKey")
        return Video.objects.all().order_by('-publish_date_time')


class AddAPIKey(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = APIKeySerializer
