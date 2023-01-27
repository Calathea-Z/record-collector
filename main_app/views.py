from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist
from .models import Records

class Record:
    def __init__(self, title, artist,year_made, img):
        self.title = title
        self.artist = artist
        self.img = img
        self.year_made = year_made
class Artist:
    def __init__(self, name, img, bio, verified_artist):
        self.name = name
        self.img = img
        self.bio = bio
        self.verified_artist = verified_artist
class RecordsList(TemplateView):
    template_name = "record_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = Records.object.all()
    
class ArtistsList(TemplateView):
    template_name = "artists_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = Artist.objects.all()
        return context
