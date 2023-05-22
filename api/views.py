from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .serializers import UploadSerializer,SignupSerializer,TemplateSerializer
from .models import Upload,TemplateModel

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

from django.contrib.auth.mixins import LoginRequiredMixin



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
        files=TemplateSerializer(TemplateModel.objects.all(),many=True) 
        return Response(files.data)

        

    #post request 
    def create(self,request):
        if  request.user.is_staff:
            file_uploaded=request.FILES.get('upload_file')
            date=request.data.get("valid_till")
            template=TemplateModel(upload_user=request.user,upload_file=file_uploaded,valid_till=date)
            template.save()
            response= "Template Successfully Uploaded"
            return Response(response)
        else:
            return Response("Access denied")
