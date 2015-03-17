from django.shortcuts import render
from rest_framework import generics

from .models import Topic, Like
from .serializers import TopicSerializer


class TopicListCreateAPIView(generics.ListCreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer

	def perform_create(self, serializer):
		topic = serializer.save()
		Like.objects.create(count=0, parent_topic=topic)
		print topic