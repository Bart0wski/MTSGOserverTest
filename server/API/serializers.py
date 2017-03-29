from rest_framework import serializers
from .models import Player, Position, Question

class PositionSerializer(serializers.ModelSerializer):

    class Meta :
        model = Position
        fields = ('x', 'y', 'z')


class PlayerSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta :
        model = Player
        fields = ('nickname','firstName','name','password','score','position')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta :
        model = Question
        fields ='__all__'