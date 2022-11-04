from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    Stage_name = serializers.CharField(max_length=100, required=True)
    Social_link = serializers.URLField(max_length=150, required=True)
    
    class Meta:
        model = Artist
        fields = '__all__'