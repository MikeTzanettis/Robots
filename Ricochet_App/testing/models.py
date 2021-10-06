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
    game = models.ForeignKey(Game,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.username
    class JSONAPIMeta:
        resource_name = "user"

class Square(models.Model):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    MULTI = 'Multi'
    BLANC = 'Blanc'
    CIRCLE='Circle'
    SQUARE='Square'
    TRIANGLE='Triangle'
    HEX='Hex'
    VORTEX='Vortex'
    colors=[(RED,'Red'),(GREEN,'Green'),(BLUE,'Blue'),(YELLOW,'Yellow'),(MULTI,'Multi'),(BLANC,'Blanc')]
    symbols=[(CIRCLE,'Circle'),(SQUARE,'Square'),(TRIANGLE,'Triangle'),(HEX,'Hex'),(VORTEX,'Vortex'),(BLANC,'Blanc')]
    posx=models.IntegerField(null=False)
    posy=models.IntegerField(null=False)
    color=models.CharField(max_length=6,choices=colors)
    symbol=models.CharField(max_length=8,choices=symbols)
    game=models.ForeignKey(Game,null=False,on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "square"

class Turn(models.Model):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    MULTI = 'Multi'
    BLANC = 'Blanc'
    CIRCLE='Circle'
    SQUARE='Square'
    TRIANGLE='Triangle'
    HEX='Hex'
    VORTEX='Vortex'
    colors=[(RED,'Red'),(GREEN,'Green'),(BLUE,'Blue'),(YELLOW,'Yellow'),(MULTI,'Multi'),(BLANC,'Blanc')]
    symbols=[(CIRCLE,'Circle'),(SQUARE,'Square'),(TRIANGLE,'Triangle'),(HEX,'Hex'),(VORTEX,'Vortex'),(BLANC,'Blanc')]
    targetC=models.CharField(max_length=6,choices=colors)
    TargetS=models.CharField(max_length=8,choices=symbols)
    turn_number=models.IntegerField(null=False,default=0)
    prev_posx=models.IntegerField(null=False)
    prev_posy=models.IntegerField(null=False)
    curr_posx=models.IntegerField(null=False)
    curr_posy=models.IntegerField(null=False)
    winner=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,null=False,on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "turn"

class Bid(models.Model):
    value=models.IntegerField(null=True)
    player=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,null=False,on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "bid"