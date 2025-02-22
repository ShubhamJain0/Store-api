from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import CustomUserModel
import pyotp
from twilio.rest import Client as TwilioClient
from decouple import config

User = get_user_model()


account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config("TWILIO_AUTH_TOKEN")
twilio_phone = config("TWILIO_PHONE")
client = TwilioClient(account_sid, auth_token)



class UserSerializer(serializers.ModelSerializer):
	class Meta:

		model = CustomUserModel
		fields = ['phone']


	def create(self, validated_data):

		user = CustomUserModel.objects.create(**validated_data)
		password = User.objects.make_random_password(length=14)
		user.set_password(password)
		user.is_active = False
		user.save()

		#Time based otp
		time_otp = pyotp.TOTP(user.key, interval=60)
		time_otp = time_otp.now()
		#Phone number must be international and start with a plus '+'   
		user_phone_number = user.phone
		user_phone_number = '+91' + user.phone
		client.messages.create(
			body="Your verification code is "+time_otp,
			from_=twilio_phone,
			to=user_phone_number
		)

		return user


class GetUserSerializer(serializers.ModelSerializer):
	class Meta:

		model = CustomUserModel
		fields = ['id', 'phone', 'name', 'email', 'image']



class EditUserSerializer(serializers.ModelSerializer):
	class Meta:

		model = CustomUserModel
		fields = ['email', 'name', 'phone', 'image', 'id']


	def update(self, instance, validated_data):
		"""Updates the user, sets password and returns user"""
		password = validated_data.pop('password', None)
		user = super().update(instance, validated_data)

		if password:
			user.set_password(password)
			user.save()

		return user
