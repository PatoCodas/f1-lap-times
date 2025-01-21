from django import forms
from .models import LapTime

class LapTimeForm(forms.ModelForm):
    class Meta:
        model = LapTime
        fields = ['track', 'time', 'date']
        widgets = {
            'time': forms.TextInput(attrs={'placeholder': 'MM:SS.mmm'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }