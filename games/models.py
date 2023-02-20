from django.db import models


class Game(models.Model):

  name = models.CharField(max_length=50)
  creator = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
