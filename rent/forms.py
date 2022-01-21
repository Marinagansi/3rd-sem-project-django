from socket import fromshare
from django import forms
from rent.models import VDetails

class RentForm(forms.ModelForm):
    class Meta:
     model = VDetails
     fields = ("__all__")