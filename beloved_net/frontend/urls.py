from django.urls import path, include

urlpatterns = [
    path('teachings/', include('frontend.frontend_urls.teaching_urls')),
]