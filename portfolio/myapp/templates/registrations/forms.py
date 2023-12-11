from django import forms

class PersonneFroms(forms.Form):
    nom = forms.CharField(max_length=50,error_messages={'required':'champ obligatoire'})
    age = forms.IntegerField()