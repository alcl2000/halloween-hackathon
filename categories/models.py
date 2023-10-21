from django.db import models

# Create your models here.


class Categories (models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.title