from socket import fromshare
from django import forms
from book_trip.models import TBooking
class tbooked(forms.ModelForm):
    class Meta:
     model = TBooking
     fields = ("__all__")