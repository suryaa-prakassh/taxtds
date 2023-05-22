from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .serializers import UploadSerializer,SignupSerializer,TemplateSerializer
from .models import Upload,TemplateModel

from django.http import HttpResponse
from django.conf import  settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import date

class UploadViewSet(LoginRequiredMixin,ViewSet):
    #serializer to parse the json to python datatypes
    serializer_class=UploadSerializer

    #post request 
    def create(self,request):
        file_uploaded=request.FILES.get('upload_file')
        response= "You have uploaded a  file"
        new_file=Upload(upload_file=file_uploaded,upload_user=request.user)
        new_file.save()
        return Response(response)

@api_view(["POST"])
def Signup(request):
    #parse json to native python format
    serializer=SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Created Successfully")


@api_view(["POST"])
def Login(request):
    try:
        username=request.data['username']
        password=request.data['password']
        user=authenticate(request,username=username,password=password)
        if not user:
            return Response("Invalid Login")
        else:
            login(request,user)
            return Response("Login Successfull")
    except:
        return Response("username and password are not valid")
    return Response("ok")


@api_view(["GET"])
@login_required(login_url="/api/login")
def Logout(request):
    logout(request)
    return Response("Logout Successfull")



class TemplateViewSet(LoginRequiredMixin,ViewSet):
    #serializer to parse the json to python datatypes
    serializer_class=TemplateSerializer
    def list(self,request):
        file =TemplateModel.objects.all()[0]
        today=date.today()
        #checking if it is valid to download
        if today <= file.valid_till:
                file_name=file.upload_file.url.split("/")
                content=open(str(settings.BASE_DIR)+"\\media\\"+file_name[-1],"rb")
                response = HttpResponse(content.read(),content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename=template.xlxs'
                return response

        return Response("No file is available ")
        

    #post request 
    def create(self,request):
        if  request.user.is_staff:
            serializer=TemplateSerializer(data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
            response= "Template Successfully Uploaded"
            return Response(response)
        else:
            return Response("Access denied")
