from django.forms import ModelForm
from django import forms
from profiles.models import createprofilemodel

class createprofileform(ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = createprofilemodel
        fields = '__all__'