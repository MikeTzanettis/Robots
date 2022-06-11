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
    obstacle=models.IntegerField(null=False)
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
    targetC=models.CharField(max_length=6,choices=colors,null=True)
    TargetS=models.CharField(max_length=8,choices=symbols,null=True)
    turn_number=models.IntegerField(default=0,null=True)
    pos_red=models.IntegerField(null=True)
    pos_blue=models.IntegerField(null=True)
    pos_green=models.IntegerField(null=True)
    pos_yellow=models.IntegerField(null=True)
    pos_black=models.IntegerField(null=True)
    sequence=models.TextField(null=True)
    winner=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,null=False,on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "turn"

class Bid(models.Model):
    value=models.IntegerField(null=True)
    player=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    game=models.ForeignKey(Game,null=False,on_delete=models.CASCADE)

    class JSONAPIMeta:
        resource_name = "bid"