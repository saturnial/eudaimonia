import datetime
from django.utils import timezone
from django.db import models


class Moment(models.Model):
  text = models.CharField(max_length=140)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.text

  def was_published_today(self):
    return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
