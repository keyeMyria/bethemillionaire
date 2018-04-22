from rest_framework import serializers
from . import models



#comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ('id', 'comment')



#subcomment serializer
class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubComment
        exclude = ('id', 'subcomment')

