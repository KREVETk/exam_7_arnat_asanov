from django import forms
from .models import GuestEntry

class GuestEntryForm(forms.ModelForm):
    class Meta:
        model = GuestEntry
        fields = ['name', 'email', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
