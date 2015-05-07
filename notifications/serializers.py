from swampdragon.serializers.model_serializer import ModelSerializer


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = 'notifications.Notification'
        publish_fields = ('message', 'verb', )
        update_fields = ('message', 'verb', )
