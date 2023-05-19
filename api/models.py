from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
from django.db import models

class Upload(models.Model):
    upload_file=models.FileField()
    upload_time=models.DateTimeField(auto_now_add=True)
    upload_user=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    modified_at=models.DateTimeField(auto_now=True)

    class  Meta:
        ordering=('-modified_at',)

    def __str__(self):
        return f"{self.upload_file}"

