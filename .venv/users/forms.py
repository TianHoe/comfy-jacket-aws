from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    PasswordChangeForm
)
from users.models import Profile

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.', widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
class ChangePWform(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={'class':'form-control', 'type':'password'}
        )
    )
    new_password1 = forms.CharField(
        label = "New Password:",
        widget = forms.PasswordInput(
            attrs={'class':'form-control', 'type':'password'}
        )
    )
    new_password2 = forms.CharField(
        label = "New Password(again):",
        widget = forms.PasswordInput(
            attrs={'class':'form-control', 'type':'password'}
        )
    )

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

class EditProfileform(UserChangeForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.', widget=forms.EmailInput(attrs={'class':'form-control'}))
    remove = forms.BooleanField(
        required = False,
        widget = forms.CheckboxInput(
            attrs = {
                "id": "remove_img",
                "style": "display:none"
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    # number = forms.IntegerField(
    #     label = "Phone Number:", 
    #     required = False, 
    #     widget = forms.NumberInput(
    #         attrs={'class':'form-control'}
    #     )
    # )

    profile_img = forms.ImageField(
        label = "Upload an image:",
        required = False,
        widget = forms.FileInput(
            attrs= {
                "class": 'form-control-file',
                'onchange': 'getUrls(this);',
                "id": "img"
            }
        ) 
    )

    # city = forms.CharField(
    #     label = "City",
    #     max_length=50, 
    #     required=False, 
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'form-control'
    #         })
    # )

    class Meta:
        model = Profile
        fields = ['profile_img']

