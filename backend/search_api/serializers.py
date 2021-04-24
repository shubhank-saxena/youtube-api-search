from rest_framework import serializers

from backend.search_api.models import Youtube


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = '__all__'
        # exclude = ('id')
