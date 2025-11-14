from rest_framework import serializers
from .models import DownloadCounter

class DownloadCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadCounter
        fields = ['id', 'name', 'count', 'created_at', 'updated_at']
        read_only_fields = ['count', 'created_at', 'updated_at']
