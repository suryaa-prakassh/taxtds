from rest_framework.serializers import FileField,Serializer,DateField
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.generics import CreateAPIView

class UploadSerializer(Serializer):
    raise_exception = True
    permission_denied_message = 'You must select an issuer.'

    #change the login url here to redirect to correct page
    login_url="/api/login"

    file_upload=FileField()

    class meta:
        fields=['file_upload']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','first_name','last_name','password']
    
    def create(self, validated_data):
        validated_data['username']=validated_data['email']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class TemplateSerializer(Serializer):
    raise_exception = True
    permission_denied_message = 'You must select an issuer.'

    #change the login url here to redirect to correct page
    login_url="/api/login"

    template=FileField()
    valid_till=DateField()

    class meta:
        fields=['template','valid_till']


