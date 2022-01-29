from socket import fromshare
from django import forms
from book_guide.models import Book_guide
class GuideForm(forms.ModelForm):
    class Meta:
     model = Book_guide
     fields = ("__all__")