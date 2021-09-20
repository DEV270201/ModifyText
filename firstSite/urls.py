"""firstSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views  #. refers to command line application. it means python will find the views file in the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    # "" is considered for home
    path("", views.home, name="home"),
    path("analyze",views.analyze, name="analyze")
    #here if you put /contact then django will understand 127.1.0.0.8000//contact
    #dont put / .. django will put it by default
    # path("contact" , views.contact , name="contact"),
    # path("image", views.image , name="image"),
    # path("removepunc" , views.removePunc, name="removepunc"),
    # path("removespace" , views.removeSpace, name="removespace"),
    # path("removenewline" , views.removeNewLine, name="removenewline"),
    # path("capfirst" , views.capFirst, name="capfirst"),
    # path("charcount" , views.charCount, name="charcount"),
]
