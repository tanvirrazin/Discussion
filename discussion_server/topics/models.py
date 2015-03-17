import datetime

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	body = models.TextField()
	created_by = models.ForeignKey(User)
	created_time = models.DateTimeField(default=datetime.datetime.now())

	def get_comments_count(self):
		return len(Comment.objects.filter(parent_topic=self))

	def get_likes_count(self):
		try:
			like = Like.objects.get(parent_topic=self)
			return like.count
		except Like.DoesNotExist:
			return 0

	def get_creator(self):
		return self.created_by.get_full_name()


class Comment(models.Model):
	body = models.TextField()
	created_by = models.ForeignKey(User)
	parent_topic = models.ForeignKey(Topic)
	created_time = models.DateTimeField(default=datetime.datetime.now())


class Like(models.Model):
	count = models.IntegerField(default=0)
	parent_topic = models.ForeignKey(Topic)
	given_by = models.ManyToManyField(User)