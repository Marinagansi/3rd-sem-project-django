from socket import fromshare
from django import forms
from booking_vehicle.models import VBooking
class vbooked(forms.ModelForm):
    class Meta:
     model = VBooking
     fields = ("__all__")