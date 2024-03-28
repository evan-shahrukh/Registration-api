from rest_framework import serializers
from ..models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    
    def save(self):
        if User.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError("Email already exists")
        user = User(username=self.validated_data["username"],email=self.validated_data["email"])
        user.set_password(self.validated_data["password"])
        user.save()
        return user
