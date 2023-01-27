from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordsList.as_view(), name=''),
    path('artists/', views.ArtistsList.as_view(), name='artists'),
]
