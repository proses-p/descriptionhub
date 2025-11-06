from .models import Member
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'description']