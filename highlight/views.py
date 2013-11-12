from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from highlight.models import Moment
from django.contrib.auth.models import User
from rest_framework import viewsets
from highlight import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class MomentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows moments to be viewed or edited.
    """
    queryset = Moment.objects.all()
    serializer_class = serializers.MomentSerializer

    def pre_save(self, obj):
      if not obj.can_user_edit(self.request.user):
        raise PermissionDenied
      obj.user = self.request.user

