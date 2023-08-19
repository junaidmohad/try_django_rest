from django import forms
from django.contrib.auth import authenticate
# from djano.contrib.auth.forms import UserCreationForm



from user_handler.models import CustomUser

class AccountAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)        #so that the password entered is not visible

    class Meta: 
        model = CustomUser
        fields = ('email')
