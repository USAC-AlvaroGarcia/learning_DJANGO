from django import forms

#Import models
class newDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)
    