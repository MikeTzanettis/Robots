from rest_framework import serializers
from testing.models import *
from django.db.models import Q
import datetime




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')