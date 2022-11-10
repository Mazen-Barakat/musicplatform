from users.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError

def validate_username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError('Username already exists, try again')
    return username

def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError('Email already exists, try again')
    return email

def validate_password(self):
    if not self['password'] or not self['confirm_password']:
        raise ValidationError("Please enter the password and its confirm.")
    if self['password'] != self['confirm_password']:
        raise ValidationError("The password does not match, try again")
    return self['password']

def validate_strong_password(password):
    if len(password) < 8:
        raise ValidationError("Password must contain at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least 1 uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least 1 lowercase letter.")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must contain at least 2 letter.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least 1 digit.")
    return password

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, validators = [validate_username], required=True)
    email = serializers.EmailField(max_length=150, validators = [validate_email], required=True)
    password = serializers.CharField(max_length=100, style = {'input_type': 'password'}, validators = [validate_strong_password], required=True)
    confirm_password = serializers.CharField(max_length=100, style = {'input_type': 'password'}, validators = [validate_strong_password], required=True)
    bio = serializers.CharField(max_length=256, required=False)
    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio')
        validators = [validate_password]