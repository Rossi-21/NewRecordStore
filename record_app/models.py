from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Group(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Record(models.Model):
    title = models.CharField(max_length=200, null=True)
    created_on =models.DateTimeField(null=True)
    artist = models.ManyToManyField(Artist, related_name="artist")
    group = models.ForeignKey(Genre, related_name='records', on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name="genre")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

