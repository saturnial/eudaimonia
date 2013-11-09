from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from highlight.models import Moment


def index(request):
  moments = Moment.objects.order_by('-timestamp')
  output = ', '.join([m.text for m in moments])
  return HttpResponse(output)


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from highlight import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class MomentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Moment.objects.all()
    serializer_class = serializers.MomentSerializer

    def pre_save(self, obj):
      if not obj.can_user_edit(self.request.user):
        raise PermissionDenied
      obj.user = self.request.user
