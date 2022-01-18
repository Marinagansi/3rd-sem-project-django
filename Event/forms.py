from socket import fromshare
from django import forms
from Event.models import event

class EventForm(forms.ModelForm):
    class Meta:
     model = event
     fields = ("__all__")