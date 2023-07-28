from django.shortcuts import render
from .models import Game
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import GameSerializer
# Create your views here.

# class GameListView(ListAPIView):
class GameListView(ListCreateAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

