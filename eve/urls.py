from django.urls import path
from django.conf.urls import url
from .views import FileUploadView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^upload/$', FileUploadView.as_view(), name='file-upload'),
]
