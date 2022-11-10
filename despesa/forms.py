from django import forms

from .models import Despesa

class DespesaForm(forms.ModelForm):
    required_css_class = 'required'
    #valor = DecimalField(max_digits=8, decimal_places=2, localize=True)
    class Meta:
        model = Despesa
        fields = ('ptrab_id','tipo_despesa_id', 'unidade_id', 'nd','valor', 'memoria_calculo')
        widgets = {
            'ptrab_id': forms.Select(attrs={'placeholder': 'PTRab', 'autofocus': True}),
            'tipo_despesa_id': forms.Select(attrs={'placeholder': 'Tipo Despesa'}),
            'unidade_id': forms.Select(attrs={'placeholder': 'OM'}),
            'nd': forms.Select(attrs={'placeholder': 'ND'}),
            'valor': forms.TextInput(attrs={'placeholder': '0,00'}),
            'memoria_calculo': forms.Textarea(attrs={'placeholder': 'Memória de Cálculo','cols': 30, 'rows': 1}),
        }
    
        
    def __init__(self, *args, **kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'