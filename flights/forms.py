from socket import fromshare
from django import forms
from flights.models import Book_guide
class EventForm(forms.ModelForm):
    class Meta:
     model = Book_guide
     fields = ("__all__")