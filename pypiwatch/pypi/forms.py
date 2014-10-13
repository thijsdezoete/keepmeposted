from django import forms
from .models import Watcher

class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=300)
    package_name = forms.CharField()
