from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('preview/<int:pk>/', views.display_preview, name='preview'),
]
