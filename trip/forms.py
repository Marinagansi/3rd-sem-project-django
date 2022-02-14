from socket import fromshare
from django import forms
from trip.models import TripPackage

class TripForm(forms.ModelForm):
    class Meta:
     model = TripPackage
     fields = ("__all__")