from socket import fromshare
from django import forms
from registration.models import Registration

class CustomerForm(forms.ModelForm):
    class Meta:
     model = Registration
     fields = ("__all__")