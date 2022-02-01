from socket import fromshare
from django import forms
from guide_booked.models import GBooking
class gbooked(forms.ModelForm):
    class Meta:
     model = GBooking
     fields = ("__all__")