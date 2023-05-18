from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from .serializers import UploadSerializer
from .models import Upload

class UploadViewSet(ViewSet):
    #serializer to parse the json to python datatypes
    serializer_class=UploadSerializer

    #list for get request
    def list(self,request):
        return Response("GET API")

    #post request 
    def create(self,request):
        file_uploaded=request.FILES.get('file_upload')
        response= "You have uploaded a  file"
        new_file=Upload(upload_file=file_uploaded,upload_user=request.user)
        new_file.save()
        return Response(response)

class DownloadView(ViewSet):


    def list(self,request):
        pass
        #to be implemented after the user feature

