from django import forms
from Proyecto_Final_Python_App.models import UsuarioEstandar

class UsuarioEstandarForm(forms.ModelForm):
    class Meta:
        model = UsuarioEstandar
        fields = ['username', 'password', 'email']
    
    is_superuser = forms.BooleanField(label='Es superusuario', required=False)