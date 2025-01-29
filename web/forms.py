from django import forms
from django.forms import ModelForm
from .models import room
from .models import update
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError

class RoomForm(ModelForm):
    class Meta:
        model=room
        fields='__all__'
        exclude = ['host']

class UpdateForm(ModelForm):
    class Meta:
        model=update
        fields='__all__'
         

class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField(required=True)  
    lastname = forms.CharField(required=True) 

    class Meta:  
        model = User  
        fields = ('username', 'email', 'lastname', 'password1', 'password2')

    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if User.objects.filter(username=username).exists():  
            raise ValidationError("This username is already taken.")  
        return username       