from django import forms
from Proyecto_Final_Python_App.models import UsuarioEstandar, Juegos

class UsuarioEstandarForm(forms.ModelForm):
    class Meta:
        model = UsuarioEstandar
        fields = ['username', 'password', 'email']
    
    is_superuser = forms.BooleanField(label='Es superusuario', required=False)
    
    
class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = '__all__'
