from socket import fromshare
from django import forms
from booking_vehicle.models import VBooking
class vbooked(forms.ModelForm):
    class Meta:
     model = VBooking
     fields = ("__all__")

class vupdatebooked(forms.ModelForm):
    class Meta:
     model = VBooking
     fields = ('address','start_date','end_date')