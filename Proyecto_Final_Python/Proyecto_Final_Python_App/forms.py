from django import forms
from Proyecto_Final_Python_App.models import UsuarioEstandar, Juegos, Comentario, Lanzamiento

class UsuarioEstandarForm(forms.ModelForm):
    class Meta:
        model = UsuarioEstandar
        fields = ['username', 'password', 'email', 'is_superuser']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = '__all__'

class AgregarComentarioForm(forms.Form):
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea(attrs={'rows': 4}), required=False)
    
class ActualizarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        

class LanzamientoForm(forms.ModelForm):
    class Meta:
        model = Lanzamiento
        fields = '__all__'