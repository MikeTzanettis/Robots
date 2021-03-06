from django.shortcuts import render
from rest_framework import viewsets
from testing.models import *
from testing.serializers import *
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def create(self, request):
        try:
            data = request.data
            s = UserSerializer(data=data)
            print("Valid data: "+str(s.is_valid()))
            if s.is_valid():
                username = data['username']
                password = data['password']
                
                
                User.objects.create_user(username=username,password=password)
                return Response(status=201, data=data)
            else:
                data = s.errors
                return Response(status=400, data=data)
        except Exception as e:
            print(e)
            return HttpResponse(status=400) 

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        print(token)
        role = token.user.role
        return Response({'token': token.key, 'role': role, 'id': token.user_id})

class SquareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = SquareSerializer
    queryset = Square.objects.all()

class TurnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = TurnSerializer
    queryset = Turn.objects.all()

class BidViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sites to be CRUDed.
    """
    serializer_class = BidSerializer
    queryset = Bid.objects.all()

def page(request,name):
    return render(request, name + ".html")

def create(self, request):
        try:
            data = request.data
            s = UserSerializer(data=data)
            print("Valid data: "+str(s.is_valid()))
            if s.is_valid():
                username = data['username']
                password = data['password']
                
                
                User.objects.create_user(username=username,password=password)
                return Response(status=201, data=data)
            else:
                data = s.errors
                return Response(status=400, data=data)
        except Exception as e:
            print(e)
            return HttpResponse(status=400) 
