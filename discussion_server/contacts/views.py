from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from contacts.models import UserProfile
from contacts.serializers import SignupSerializer, UserSerializer, UserProfileSerializer


class SignupView(APIView):

	def post(self, request):
		serializer = SignupSerializer(data=request.data)

		if serializer.is_valid():
			user = User.objects.create_user(serializer.data['username'], serializer.data['email'], serializer.data['password'])
			user.first_name = serializer.data['first_name'];
			user.last_name = serializer.data['last_name'];
			user.save()
			return Response({ "result": True})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListCreateAPIView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
	serializer_class = UserProfileSerializer

	def get_object(self):
		return UserProfile.objects.get(user=self.request.user)

