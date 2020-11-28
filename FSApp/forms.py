from django import forms
from django.forms import ModelForm
from .models import User

# our new form
class ContactForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"