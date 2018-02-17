"""cormacsblog URL Configuration

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
import posts.views
import sitePages.views

#   allow display of images
from django.conf.urls.static import static  # allow us view images
from django.conf import settings            # retrieve values from the settings file

urlpatterns = [
    url(r'^admin/', admin.site.urls),   # recommended to change URL from admin/ to sokething else
    url(r'^$', posts.views.index),
    url(r'^posts/',include('posts.urls')),
    url(r'^about/', sitePages.views.about, name="about")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # allows display of images
