"""MyURLSaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from  MyURLSaver_app import views as core_views
from django.contrib.auth import views as auth_views

urls1 = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$',core_views.LogoutView, name="logout"),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^addurls/$', core_views.addurls, name='addurls'),
    url(r'^delurls/$', core_views.delurls, name='delurls'),
    url(r'^seeurls/$', core_views.seeurls, name='seeurls'),
    url(r'^admin/', admin.site.urls),
    ]
   

urlpatterns = [
    url(r'^MyURLSaver/', include(urls1)),

    ]



