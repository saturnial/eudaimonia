import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)


class Moment(models.Model):
  text = models.CharField(max_length=140)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  date = models.DateField()
  user = models.ForeignKey(User)

  class Meta:
    ordering = ('created',)

  def __unicode__(self):
    return self.text

  def was_published_today(self):
    return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

  def can_user_edit(self, user):
    return user == self.user or not user

class Like(models.Model):
  liker = models.ForeignKey(User)
  moment = models.ForeignKey(Moment)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
  inviter = models.ForeignKey(User, related_name='inviter')
  inivitee = models.ForeignKey(User, related_name='invitee')
  confirmed = models.BooleanField(default=False)
  reviewed = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

class FriendTag(models.Model):
  moment = models.ForeignKey(Moment)
  friend_tagged = models.ForeignKey(User)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

class PushNotification(models.Model):
  user = models.ForeignKey(User)
  notification_type = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
