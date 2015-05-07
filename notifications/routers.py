from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter

from .serializers import NotificationSerializer
from .models import Notification


class NotificationRouter(ModelPubRouter):
    serializer_class = NotificationSerializer
    model = Notification
    route_name = 'notification'
    valid_verbs = ['subscribe']

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

    def get_subscription_contexts(self, **kwargs):
        return {'user__id': self.connection.user.pk}


route_handler.register(NotificationRouter)
