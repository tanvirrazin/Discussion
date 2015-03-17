from django.contrib.auth.models import User
from rest_framework import serializers

from contacts.models import UserProfile


class SignupSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=20)
	password = serializers.CharField(min_length=5, max_length=10)
	first_name = serializers.CharField(max_length=50, required=False)
	last_name = serializers.CharField(max_length=50, required=False)
	email = serializers.CharField(max_length=50)
	birthday = serializers.DateField()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile