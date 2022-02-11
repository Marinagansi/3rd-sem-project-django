from socket import fromshare
from django import forms
from book_flights.models import FBooking
class fbooked(forms.ModelForm):
    class Meta:
     model = FBooking
     fields = ("__all__")