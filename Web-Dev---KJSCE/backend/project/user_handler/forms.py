from django import forms
from django.contrib.auth import authenticate
# from djano.contrib.auth.forms import UserCreationForm



from user_handler.models import CustomUser

class AccountAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)        #so that the password entered is not visible

    class Meta: 
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login.")

#this form function is responsible for updating the details of the respective user
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)       #here instance means to get the primary key of the user
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % customuser.email)
        
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(username.username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % customuser.username)