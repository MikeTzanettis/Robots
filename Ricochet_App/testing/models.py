from django.db import models

# Create your models here.
class Game(models.Model):
    turn_number = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    targets_remaining = models.IntegerField(default=17)
    
    class JSONAPIMeta:
        resource_name = "game"
