from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Defining the password field using serializers.CharField()
    password = serializers.CharField(write_only=True)  # Ensures password is write-only

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Creating the user with the validated data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Uses CharField for password input
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        # Generate and assign a token to the newly created user
        Token.objects.create(user=user)
        return user
