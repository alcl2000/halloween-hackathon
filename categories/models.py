from django.db import models

# Create your models here.


class Categories (models.Model):
    title = CharField(max_length=255, blank=False)
    posts = ForiegnKey()