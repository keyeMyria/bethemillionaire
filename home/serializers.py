from rest_framework import serializers
from . import models


class LiveChatMessageSerializers(serializers.ModelSerializer):
    chat_user = serializers.CharField(source='user.username')

    class Meta:
        model = models.LiveChatMessage
        fields = ('room', 'message', 'user', 'chat_user')
