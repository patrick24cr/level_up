from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = description = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False,)
    time = models.TimeField(auto_now=False, auto_now_add=False,)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)