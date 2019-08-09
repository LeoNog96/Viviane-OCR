from django.urls import path
from . import views


urlpatterns = [
    path('api/ocr/queue',views.FileQueueView.as_view()),
    path('api/ocr/file-upload', views.FileUploadView.as_view())
]