"""
URL configuration for stud_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

# router.register("v2/student/",student_apiview,basename= "stud"),
# router.register("v2/student/<int:pk>",studentmixin,basename= "stud")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",AdminRegistrationView.as_view(),name="reg"),
    path("login/",AdminLoginView.as_view(),name="login"),
    path('login1/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("department/",DepartmentAPIView.as_view(),name="dpt"),
    path("stud_prof/",StudProfileAPIView.as_view(),name="stud_pro"),
    path("list_all/",StudentListView.as_view(),name="list"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    
]+router.urls



