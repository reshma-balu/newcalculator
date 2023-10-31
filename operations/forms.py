from django import forms

class UperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()