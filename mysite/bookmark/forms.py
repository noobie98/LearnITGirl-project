import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
import datetime #for checking renewal date range.
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
User = get_user_model()
class signUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput,required = True,max_length = 30,label = 'Email')
    first_name=forms.CharField(label = 'First name',widget=forms.TextInput,required = True, max_length = 30)
    last_name=forms.CharField(label = 'Last name',widget=forms.TextInput,required = False,max_length = 30)

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2'
            )

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one"))
    def clean_password(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
    def save(self,commit=True):
        user=super(signUpForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()
        return user
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username = username ,password = password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password:
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm,self).clean(*args,**kwargs)