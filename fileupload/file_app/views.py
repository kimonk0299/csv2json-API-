from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .csv2json import convert2json 
from .serializers import FileSerializer
from django.conf import settings
from django.http import JsonResponse

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()   
      filenme = file_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)
      print (location)
      return Response(convert2json(location))
      return (hello)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)