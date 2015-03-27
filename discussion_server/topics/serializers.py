from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):

	comments_count = serializers.IntegerField(source='get_comments_count')
	likes_count = serializers.IntegerField(source='get_likes_count')
	creator = serializers.CharField(source='get_creator')
	class Meta:
		model = Topic


class TopicLikeDislikeSerializer(serializers.Serializer):

	like = serializers.BooleanField()
