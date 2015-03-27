from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Topic, Like
from .serializers import TopicSerializer


class TopicListCreateAPIView(generics.ListCreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer

	def perform_create(self, serializer):
		topic = serializer.save()
		Like.objects.create(count=0, parent_topic=topic)
		print topic


class TopicLikeDislikeAPIView(APIView):
	permission_classes = ()

	def put(self, request, pk, format=None):
		try:
			like_data = Like.objects.get(parent_topic_id=pk)
		except Like.DoesNotExist:
			like_data = Like(count=0, parent_topic_id=pk)
			like_data.save()

		like_data.count = like_data.count + 1
		like_data.given_by.add(request.user)
		like_data.save()
		return Response({"success": True }, status.HTTP_200_OK)

