from django import forms
from .models import BuyList

class BuyListForm(forms.ModelForm):
    class Meta:
        model = BuyList
        fields = ['watch', 'profil']