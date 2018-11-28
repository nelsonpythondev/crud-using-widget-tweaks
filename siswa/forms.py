from django import forms
from .models import Siswa

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ('name', 'male', 'address', )
