from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.blog),
    path('<int:blog_id>/',views.blog_text)
]
