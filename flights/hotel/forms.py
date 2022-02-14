from socket import fromshare
from django import forms
from hotel.models import Hotel, HBooking
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


class HotelFormStepThree(forms.ModelForm):
    class Meta:
     model = Hotel
     fields=("parking","Breakfast")


class HotelFormStepFour(forms.ModelForm):
    class Meta:
     model = Hotel
     fields=("image1","image2")
    
class HotelFormStepFive(forms.ModelForm):
    class Meta:
     model = Hotel
     fields=("cancelation","Day_of_payment","Hotel_description","check_in_from","check_in_to","check_out_from","check_out_to","pet")
  
class Hbooked(forms.ModelForm):
    class Meta:
     model = HBooking
     fields=("__all__")