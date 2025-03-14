from django.urls import path
from posts import views as post_views

urlpatterns = [
    path('', post_views.TeachingListAPIView.as_view()),
    path('<int:teaching_id>/', post_views.TeachingDetailAPIView.as_view()),
]
