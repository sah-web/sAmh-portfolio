from django.contrib import admin
from django.urls import path, include
from home import views
import os

# Django Admin Header Customization
admin.site.site_header = "Login to Developer sAmH"
admin.site.site_title = "Welcome to sAmH's Dashboard"
admin.site.index_title = "Welcome to this Portal"


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
]
