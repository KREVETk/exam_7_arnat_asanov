from django import forms
from .models import GuestEntry

class GuestEntryForm(forms.ModelForm):
    class Meta:
        model = GuestEntry
        fields = ['name', 'email', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }

class SearchForm(forms.Form):
    name = forms.CharField(
        label='Имя автора',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поиск по имени'})
    )
