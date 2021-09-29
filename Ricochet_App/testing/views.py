from django.shortcuts import render
from rest_framework import viewsets
from testing.models import *
from testing.serializers import *
# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    