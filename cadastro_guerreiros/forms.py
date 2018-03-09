from django import forms
from .models import guerreiros


# MASCARA = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )
#
# LUVA = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )
#
# MARCADOR = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )
#
# FARDA = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )
#
# RADIO = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )
#
# COLETE = (
#     ('S', 'Sim'),
#     ('N', 'Não'),
# )


class FormCadastroGuerreiros(forms.ModelForm):
    nome = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}))
    telefone = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '62 9 9999-9999'}))
    endereco = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Rua 1 Qd: 02 Lt: 01 Bairro Tal'}))
    instagram = forms.CharField(max_length=50,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'seu_nick'}))
    facebook = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'seu_nick ou link'}))
    contato_emergencia = forms.CharField(max_length=50,
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control', 'placeholder': 'Mãe 62 9 9999-9999'}))
    tipo_sanguineo = forms.CharField(max_length=50,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'O+'}))
    alergia_medicamento = forms.CharField(max_length=50,
                                          widget=forms.TextInput(
                                              attrs={'class': 'form-control',
                                                     'placeholder': 'Sim Dipirona'}))
    mascara = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)
    luva = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)
    marcador = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)
    farda = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)
    radio = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)
    colete = forms.ChoiceField(choices=((1, 'Sim'), (0, 'Nao')), required=False)

    class Meta:
        model = guerreiros
        fields = '__all__'
