import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Moment(models.Model):
  text = models.CharField(max_length=140)
  created_timestamp = models.DateTimeField(auto_now_add=True)
  modified_timestamp = models.DateTimeField(auto_now=True)
  date = models.DateField()
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.text

  def was_published_today(self):
    return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

class Like(models.Model):
  liker = models.ForeignKey(User)
  moment = models.ForeignKey(Moment)
  created_timestamp = models.DateTimeField(auto_now_add=True)
  modified_timestamp = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
  inviter = models.ForeignKey(User)
  inivitee = models.ForeignKey(User)
  confirmed = models.BooleanField(default=False)
  reviewed = models.BooleanField(default=False)
  created_timestamp = models.DateTimeField(auto_now_add=True)
  modified_timestamp = models.DateTimeField(auto_now=True)

class FriendTag(models.Model):
  moment = models.ForeignKey(Moment)
  friend_tagged = models.ForeignKey(User)
  created_timestamp = models.DateTimeField(auto_now_add=True)
  modified_timestamp = models.DateTimeField(auto_now=True)

class PushNotification(models.Model):
  user = models.ForeignKey(User)
  notification_type = models.CharField()
  created_timestamp = models.DateTimeField(auto_now_add=True)
  modified_timestamp = models.DateTimeField(auto_now=True)
