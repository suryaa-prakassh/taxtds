from rest_framework.serializers import FileField,Serializer,DateField
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from .models  import  TemplateModel,Upload
 
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields=['upload_file']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','first_name','last_name','password']
    
    def create(self, validated_data):
        validated_data['username']=validated_data['email']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model=TemplateModel
        fields=['upload_file','valid_till']

    def create(self,validated_data):
        request=self.context.get("request")
        validated_data['upload_user']=request.user
        TemplateModel.objects.all().delete()

        return super().create(validated_data) 
