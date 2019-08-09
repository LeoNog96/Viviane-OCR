from django.shortcuts import render
from rest_framework import generics,views
from .models import File
from .serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

class FileUploadView(views.APIView):

    parser_classes = (MultiPartParser,)

    def put(self, request, format=None):
        
        file_obj = request.FILES['file']
        file = File()

        # file.file_name = 
        # file.extension = format
        # file.length = file_obj.length()

        return Response(status=204)

class FileQueueView(generics.ListAPIView):
    
    serializer_class = FileSerializer
    def get_queryset(self):
        return File.objects.filter(done=False)