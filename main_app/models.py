from django.db import models

class Artist(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Records(models.Model):

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    year_made = models.TextField(max_length=500)
    img = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['title']