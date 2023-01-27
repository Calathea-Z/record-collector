from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Record:
    def __init__(self, title, artist, image, year_made, label, _id, condition):
        self.title = title
        self.artist = artist
        self.image = image
        self.year_made = year_made
        self.label = label
        self.id = _id
        self.condition = condition

img_address =  "https://images.genius.com/1f61e7c20f3ec7d82362ab7034328abe.1000x980x1.jpg"       

records = [
    Record("Let It Be", "The Beatles", img_address, 1970, "Apple", "REFJJFNCHF*#$&*#$(*", "VERY GOOD" )
]

class RecordsList(TemplateView):
    template_name = "record_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = records 
        return context
