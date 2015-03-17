from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User)
	screen_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	country = models.CharField(max_length=100, choices=(
		('Bangladesh', 'Bangladesh'),
		('Japan', 'Japan'),
		('Bhutan', 'Bhutan'),
		('Korea', 'Korea'),
	), default='Bangladesh')
