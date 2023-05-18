
from django.urls import path,include
from .views import UploadViewSet,test
from rest_framework import routers

#for generating automatic url patterns
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns=[
    path('',include(router.urls)),
    path('test/',test,name="test"),
]
