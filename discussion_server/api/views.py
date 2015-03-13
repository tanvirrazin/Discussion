from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers.auth_serializers import LoginSerializer


class LoginView(APIView):

    def post(self, request,):
        print request.data
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({ "result": True })
            else:
                return Response({ "result": "User is deactivated" }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ "result": "Incorrect combination of Username and Password" }, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response({ "result": True })
