from socket import fromshare
from django import forms
from hotel.models import Hotel
class HotelForm1(forms.ModelForm):
    class Meta:
     model = Hotel
     fields = ("hotel_name","contact_name","phonenumber","hotel_address","hotel_region")

class HotelForm2(forms.ModelForm):
    class Meta:
     model = Hotel
     fields = ("room_type","smoking_policy","no_of_rooms","Beds","no_of_guest")


class HotelFormStepOne(forms.ModelForm):
    class Meta:
     model = Hotel
     fields = ("hotel_name","contact_name","phonenumber","hotel_address","hotel_region")


class HotelFormStepTwo(forms.ModelForm):
    class Meta:
     model = Hotel
     fields = ("room_type","smoking_policy","no_of_rooms","Beds","no_of_guest")

    
