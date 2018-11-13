"""BBS URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from mybbs import views
from django.views.static import serve
from BBS import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^pc-geetest/register', views.pc_geetest),

    url(r'^get_code/', views.get_code),
    url(r'^index/', views.index),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
    url(r'^backhome/', views.back_home),
    url(r'^addarticle/', views.addarticle),
    url(r'^diggit/', views.diggit),
    url(r'^comment/', views.comment),
    url(r'^media/(?P<path>.*)', serve,{'document_root':settings.MEDIA_ROOT}),
    # url(r'^test/', views.test,{'xx':'dfafas'}),


    # lqz/article/123
    url(r'^(?P<username>\w+)/article/(?P<pk>\d+)', views.article_detail),
    url(r'^(?P<username>\w+)/(?P<condition>tag|category|time)/(?P<search>.*)', views.homesite),
    url(r'^(?P<username>\w+)/', views.homesite),
]
