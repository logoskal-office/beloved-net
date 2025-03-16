from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404

from rest_framework .views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .serializers import *

class TeachingListAPIView(generics.ListCreateAPIView):
    queryset = Teaching.objects.order_by('pk')
    serializer_class = TeachingSerializer

    search_fields = ['=title', 'description']
    ordering_fields = ['pk', 'date']    

    def get_permissions(self):
        self.permission_classes = [permissions.AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    
class TeachingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teaching.objects.order_by('seriespart__position')
    serializer_class = TeachingSerializer
    lookup_url_kwarg = 'teaching_id'

    def get_permissions(self):
        self.permission_classes = [permissions.AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
    
class SeriesListAPIView(generics.ListCreateAPIView):
    queryset = Series.objects.order_by('pk')
    serializer_class = SeriesSerializer

    search_fields = ['=title', 'description']
    ordering_fields = ['pk', 'date']  

    def get_permissions(self):
        self.permission_classes = [permissions.AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

class SeriesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesDetailSerializer
    lookup_url_kwarg = 'series_id'

    def get_permissions(self):
        self.permission_classes = [permissions.AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

def teachings(request):
    return render(request, 'posts/teachings/teachings.html', {'teachings': Teaching.objects.all()})

def teaching(request, teaching_id):
    teaching = get_object_or_404(Teaching, pk=teaching_id)
    
    return render(request, 'posts/teachings/teaching.html', {'teaching': teaching})

def audio(request, id):
    file = Teaching.objects.get(pk=id)
    file = file.file.path
    response = FileResponse(open(file, 'rb'), as_attachment=True, content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; filename="audio.mp3"'
    return response