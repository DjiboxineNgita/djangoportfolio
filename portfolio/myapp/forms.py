from django import forms

class VisiteurFroms(forms.Form):
    nom = forms.CharField(max_length=50,error_messages={'required':'champ obligatoire'})
    Poste = forms.IntegerField()
    date = forms.DateTimeField(auto_now_add=True)