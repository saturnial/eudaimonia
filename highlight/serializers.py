from django.contrib.auth.models import User, Group
from rest_framework import serializers
from highlight import models
from rest_framework import permissions
from highlight import permissions as custom_permissions


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')


class MomentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Moment
    fields = ('url', 'text', 'date')
    permissions = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly,)
