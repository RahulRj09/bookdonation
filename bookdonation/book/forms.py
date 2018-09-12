from django.contrib.auth.models import User
from .models import *
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio','location','birth_date')

# class UploadImageForm(forms.Form):
# 	book_images=

class BookForm(forms.ModelForm):



    class Meta:
        model = Book
        fields = ('email','booktitle', 'authorname', 'description', 'languages', 'image')


class AdduserForm(forms.ModelForm):



    class Meta:
        model = Book_request
        fields = ('Name', 'Address', 'MobileNumber', 'PinCode')