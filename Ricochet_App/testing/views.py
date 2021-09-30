from django.shortcuts import render
from rest_framework import viewsets
from testing.models import *
from testing.serializers import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request,'register.html')