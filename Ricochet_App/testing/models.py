from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Game(models.Model):
    turn_number = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    targets_remaining = models.IntegerField(default=17)
    
    class JSONAPIMeta:
        resource_name = "game"

class User(AbstractUser):
    role = models.TextField(default="admin")
    points = models.IntegerField(default=0)
    game_id = models.ForeignKey(Game,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.username
    class JSONAPIMeta:
        resource_name = "user"

    

