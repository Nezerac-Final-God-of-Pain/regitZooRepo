from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import zooBooking

# - Register or Create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - make a zoo booking
class zoobook(forms.ModelForm):
    class Meta:
        model = zooBooking
        fields = ['first_name', 'email', 'address', 'arriveDate', 'leaveDate', 'numAdults', 'numChildren', 'numInfants']

