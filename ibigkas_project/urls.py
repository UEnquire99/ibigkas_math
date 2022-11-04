"""ibigkas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.views.static import serve
from django.urls import re_path as url
from django.conf import settings

urlpatterns = [
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')), 
    path('admin/', admin.site.urls),
    path('singleplayer/', include("singlePlayer.urls")),
    path('multiplayer/', include("multiPlayer.urls")),
    path('', include("Assessment.urls")),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]


admin.site.index_title = "Ibigkas"
admin.site.site_header = "Ibigkas Web Application Admin"
admin.site.site_title = "Ibigkas Admin"


# snake_case python 
# camelCase JS 
# kebab-case CSS  
