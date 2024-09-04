from django.db import models
from django.db.models import (
    DO_NOTHING, CharField, Model, DateField, DateTimeField, ForeignKey, IntegerField, TextField
)

# Create your models here.

class Genre(Model):
    name = CharField(max_length=128)

class Rower(Model):
    nazwa = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rodzaj = TextField()
    ilosc = IntegerField()