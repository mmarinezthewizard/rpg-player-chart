from django import forms
from .models import PlayerModel

class ChartForm(forms.ModelForm):
    class Meta:
        model = PlayerModel
        fields = '__all__'

