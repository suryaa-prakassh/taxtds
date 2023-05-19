from rest_framework.serializers import FileField,Serializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.generics import CreateAPIView

class UploadSerializer(Serializer):

    file_upload=FileField()
    class meta:
        fields=['file_upload']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)



