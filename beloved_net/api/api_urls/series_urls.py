from django.urls import path
from posts import views as post_views

urlpatterns = [
    path('', post_views.SeriesListAPIView.as_view()),
    path('<int:series_id>/', post_views.SeriesDetailAPIView.as_view()),
]
