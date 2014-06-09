from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Selfie(TimeStampedModel, models.Model):
    caption = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255, null=False, blank=False)
    imageSize = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey('users.User', null=False, blank=False)
    isDeleted = models.BooleanField(default=False, null=False, blank=False)
    imageUrl = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        return self.caption + self.imageUrl

class Like(TimeStampedModel, models.Model):
    user = models.ForeignKey('users.User', null=False, blank=False)
    selfie = models.ForeignKey('core.Selfie', null=False, blank=False)
