from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Graduate, Event, Resource, Mentor, Question, Answer, Advice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GraduateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Graduate
        fields = ['firstName', 'lastName', 'jobTitle', 'location', 'linkedInLink', 'sageEmailAddress']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'location', 'date']

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['title', 'url', 'category']

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['user', 'firstName', 'lastName', 'jobTitle', 'location', 'linkedInLink', 'sageEmailAddress','expertise' ]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['subject', 'body']

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['body']

class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = ['body']