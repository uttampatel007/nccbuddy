from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import	Profile


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email','password')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self, validate_data):
		user = User(
			email = validate_data['email'],
			username = validate_data['username']
		)
		user.set_password(validate_data['password'])
		user.save()
		Token.objects.create(user=user)
		return user