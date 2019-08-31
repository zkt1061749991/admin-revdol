"""Revdol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewspip install pillow
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path, include
from .settings import MEDIA_ROOT  # 上传媒体加载包
from .settings import STATIC_ROOT
from django.views.static import serve  # 上传媒体加载包
from extra_apps import xadmin

# 进行路由的配置
urlpatterns = [
    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 富文本相关URL
    path('', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 指定上传媒体位置
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
