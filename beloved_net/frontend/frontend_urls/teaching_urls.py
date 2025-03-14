from django.urls import path
from posts import views as post_views

urlpatterns = [
    path('', post_views.teachings),
    path('<int:teaching_id>/', post_views.teaching),
]
