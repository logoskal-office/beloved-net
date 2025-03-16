from rest_framework import serializers
from .models import *

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('__all__')

class SeriesPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('__all__')

class TeachingSerializer(serializers.ModelSerializer):
    series = serializers.CharField(max_length=100, source='series.first')
    class Meta:
        model = Teaching
        fields = [
            'title',
            'description',
            'subtitle',
            'date',
            'file',
            'image',
            'series',
        ]

class SeriesDetailSerializer(serializers.ModelSerializer):
    teaching = SeriesPartSerializer('seriespart_set', many=True)
    # position = serializers.IntegerField(source='seriespart.first.position')
    class Meta:
        model = Series
        fields = ['id', 'teaching']
