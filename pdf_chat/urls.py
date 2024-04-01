from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('index/', views.index, name='index'),
    path('chats/', views.chats, name='chats'),  # Add this line
]
