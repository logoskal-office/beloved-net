from django.urls import path, include

from .views import audio

urlpatterns = [
    path('teachings/', include('api.api_urls.teaching_urls')),
    path('series/', include('api.api_urls.series_urls')),
    path('audio/<int:id>', audio, name='audio-server')
]
