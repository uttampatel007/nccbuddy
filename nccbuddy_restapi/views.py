from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .serializers import ProfileSerializer, UserSerializer
from users.models import Profile

# class ProfileDetailView(APIView):
# 	def get(self,request,pk):
# 		profile = get_object_or_404(Profile,pk=pk)
# 		data = ProfileSerializer(profile).data
# 		return Response(data)


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserCreateView(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer


class LoginView(APIView):
	permission_classes = ()

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')
		user = authenticate(username=username, password=password)
		if user:
			return Response({
				"token": user.auth_token.key
				})
		else:
			return Response(
				{
				"error": "Wrong Credentials"
				},
				status=status.HTTP_400_BAD_REQUEST
			)



