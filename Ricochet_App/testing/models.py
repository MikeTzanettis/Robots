from django.db import models

# Create your models here.
class Game(models.Model):
    turn_number = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    targets_remaining = models.IntegerField(default=17)
    
    class JSONAPIMeta:
        resource_name = "game"

class Player(models.Model):
    name = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=20,null=False)
    points = models.IntegerField(default=0)
    game_id = models.ForeignKey(Game,on_delete=models.SET_NULL,null=True)

    class JSONAPIMeta:
        resource_name = "player"

