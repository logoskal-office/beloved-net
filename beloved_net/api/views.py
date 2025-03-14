from django.shortcuts import render

from django.http import FileResponse, Http404

from posts import models as post_models

def audio(request, id):
    teaching = post_models.Teaching.objects.get(pk=id)
    if teaching.file:
            response = FileResponse(teaching.file.open('rb'), content_type='audio/mpeg')
            response['Content-Length'] = teaching.file.size
            response['Accept-Ranges'] = 'bytes'
            return response