from django import forms
from .models import RegisterForm
 
class MyRegisterForm(forms.ModelForm):
    class Meta:
        model= RegisterForm
        fields= ["Studyname","study_description","study_phase","sponsor_name"]
 