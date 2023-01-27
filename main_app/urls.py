from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordsList.as_view(), name=''),
    path('about/', views.About.as_view(), name='about'),
]
