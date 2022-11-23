from django.db import models
from .event import Event
from .gamer import Gamer

class Event_gamer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)