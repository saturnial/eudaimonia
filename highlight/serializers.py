from django.contrib.auth.models import User, Group
from rest_framework import serializers
from highlight import models
from rest_framework import permissions


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'password', 'email', 'groups')
    permissions = 

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')


class MomentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Moment
    fields = ('url', 'text', 'date')
    permissions = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
