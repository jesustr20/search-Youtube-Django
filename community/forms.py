from django import forms
from django.forms import widgets


class SearchYoutubeForm(forms.Form):
    q = forms.CharField(max_length=50)

    widgets = {
        'q': forms.TextInput(attrs={'Placeholder': 'Search'})
    }
