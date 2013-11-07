from django.db import models


class Moment(models.Model):
  text = models.CharField(max_length=140)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.text
