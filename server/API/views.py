from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Position, Question
from .serializers import PlayerSerializer, PositionSerializer, QuestionSerializer


# list all players
# players/
class PlayerList(APIView):
    """
    get:
    Return a list of all the existing players.

    post:
    Create a new user instance
    """
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
    """
    get:
    Return the details of a specific player
    """
    def get(self, request, pk):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(player, many=False)
        return Response(serializer.data)

    def post(self):
        pass

#list all questions
# questions/
class QuestionList(APIView):

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self):
        pass