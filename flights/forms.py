from socket import fromshare
from django import forms
from flights.models import Flights
class EventForm(forms.ModelForm):
    class Meta:
     model = Flights
     fields = ("__all__")