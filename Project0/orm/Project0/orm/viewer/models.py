from django.db import models
from django.db.models import (
    CharField, Model, DO_NOTHING, DateField, DateTimeField, ForeignKey, IntegerField, TextField
)

# Create your models here.

class Genre(Model):
    name = CharField(max_length=128)

class Bike(Model):
    name = CharField(max_length=128)
    price = IntegerField()
    qty = IntegerField()
    description = TextField()
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
