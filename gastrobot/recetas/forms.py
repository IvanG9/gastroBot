from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'pasos', 'tiempo_preparacion', 'imagen']

class RecetaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Quitar texto automático del ClearableFileInput
        self.fields['imagen'].widget.clear_checkbox_label = ''
        self.fields['imagen'].widget.initial_text = ''
        self.fields['imagen'].widget.input_text = ''

    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'tiempo_preparacion', 'imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'hidden',  # se oculta porque lo llamas con <label for="id_imagen">
                'accept': 'image/*'  # opcional: solo permite imágenes
            })
        }