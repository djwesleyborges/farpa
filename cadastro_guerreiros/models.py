from django.db import models


class guerreiros(models.Model):
    NAO = 0
    SIM = 1

    TIPO_CHOICES = (
        (SIM, 'Sim'),
        (NAO, 'Não'),
    )

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

    nome = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=50, null=True)
    endereco = models.CharField(max_length=150, null=False)
    instagram = models.CharField(max_length=50, null=True)
    facebook = models.CharField(max_length=100, null=True)
    contato_emergencia = models.CharField(max_length=150, null=False)
    tipo_sanguineo = models.CharField(max_length=3, null=True)
    alergia_medicamento = models.CharField(max_length=100, null=True)
    mascara = models.IntegerField(choices=TIPO_CHOICES)
    luva = models.IntegerField(choices=TIPO_CHOICES)
    marcador = models.IntegerField(choices=TIPO_CHOICES)
    farda = models.IntegerField(choices=TIPO_CHOICES)
    radio = models.IntegerField(choices=TIPO_CHOICES)
    colete = models.IntegerField(choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome