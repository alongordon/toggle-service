"""toggle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from inventit import views
from toggle.custom_admin import CustomAdmin

admin.site.login = CustomAdmin().login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.summary, name='summary'),
    url(r'^capture1', views.capture1, name='capture1'),
    url(r'^capture2', views.capture2, name='capture2'),
    url(r'^capture3', views.capture3, name='capture3'),
    url(r'^save_data/', views.save_data, name='save_data'),
    url(r'^save_count_summary/', views.save_count_summary, name='save_count_summary'),
    url(r'^export', views.export, name='export'),
    path('sign_off/<int:count>/', views.sign_off, name='sign_off'),
]
