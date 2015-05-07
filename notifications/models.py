from django.db import models
from django.contrib.auth.models import User

from swampdragon.models import SelfPublishModel

from .serializers import NotificationSerializer


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    verb = models.CharField(null=True, default='achieved', max_length=20)
    user = models.ForeignKey(User)
