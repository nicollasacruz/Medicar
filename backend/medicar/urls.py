"""medicar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework.authtoken import views

try:
    from medicar.routers import router
except:
    warnings.warn("*** problemas de importação com os routers  ***")
    router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api-auth/', include(views.obtain_auth_token, name='api-tokn-auth')),
    url(r'^api/', include(router.urls)),
]
