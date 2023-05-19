
from django.urls import path,include
from .views import UploadViewSet,Signup,Login,TemplateViewSet,Logout
from rest_framework import routers

#for generating automatic url patterns
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
router.register(r'template',TemplateViewSet,basename="template")

urlpatterns=[
    path('',include(router.urls)),
    path('signup/',Signup,name="signup"),
    path('login/',Login,name="login"),
    path('logout/',Logout,name="logout"),
        ]

