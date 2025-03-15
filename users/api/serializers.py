from rest_framework import serializers
from users.models import UserProfil

class UserProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfil
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfil
        fields = ['first_name', 'last_name', 'email', 'username','phone']
        
        


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=13, required=True)