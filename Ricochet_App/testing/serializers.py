from rest_framework import serializers
from testing.models import *
from django.db.models import Q
import datetime




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        
        fields = ('__all__')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        
        fields = ('__all__')
