from rest_framework.serializers import Serializer,FileField

class UploadSerializer(Serializer):

    file_upload=FileField()
    class Meta:
        fields=['file_upload']
