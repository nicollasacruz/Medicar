from rest_framework import serializers
from django.contrib.auth import get_user_model

  
class UserSerializer(serializers.ModelSerializer): 
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['username'], validated_data['email'],
            validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('id', 'url', 'username', 'email', 'password')

