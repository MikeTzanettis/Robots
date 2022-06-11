from rest_framework import serializers
from testing.models import *
from django.db.models import Q
import datetime




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ('__all__')

class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = ('__all__')

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('__all__')
