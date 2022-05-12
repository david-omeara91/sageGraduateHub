from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Graduate


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
