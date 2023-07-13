from rest_framework import serializers
from .models import CustomUser

#Registration Serializer
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    email = serializers.EmailField()
    name=serializers.CharField()
    number=serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('email','name','number', 'password','password2')
        extra_kwargs={
            'password':{'write_only':True}
        }
    #function to validate    
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if(password!=password2):
            raise serializers.ValidationError("Both passwords are different!")
        return attrs    
    #function to validate user    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

#Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=CustomUser
        fields=('email','password')
#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('email','name')