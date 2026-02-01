from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos =models.CharField(max_length=120)
    fotografia = models.ImageField(null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)

class Direccion(models.Model):
    contacto = models.OneToOneField(Contacto, on_delete=models.CASCADE, related_name='direccion')
    calle = models.CharField(max_length=255)
    no_ext = models.CharField(max_length=10)
    no_int = models.CharField(max_length=10, null=True)
    colonia = models.CharField(max_length=255)
    municipio =  models.CharField(max_length=255)
    referencias =  models.TextField(blank=True, default="")
    ESTADOS_MEXICO = [
        ('AGS', 'Aguascalientes'),
        ('BCN', 'Baja California'),
        ('BCS', 'Baja California Sur'),
        ('CAM', 'Campeche'),
        ('CHP', 'Chiapas'),
        ('CHH', 'Chihuahua'),
        ('CDX', 'Ciudad de México'), 
        ('COA', 'Coahuila'),
        ('COL', 'Colima'),
        ('DUR', 'Durango'),
        ('GUA', 'Guanajuato'),
        ('GRO', 'Guerrero'),
        ('HID', 'Hidalgo'),
        ('JAL', 'Jalisco'),
        ('MEX', 'Estado de México'),
        ('MIC', 'Michoacán'),
        ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'),
        ('NLE', 'Nuevo León'),
        ('OAX', 'Oaxaca'),
        ('PUE', 'Puebla'),
        ('QUE', 'Querétaro'),
        ('ROO', 'Quintana Roo'),
        ('SLP', 'San Luis Potosí'),
        ('SIN', 'Sinaloa'),
        ('SON', 'Sonora'),
        ('TAB', 'Tabasco'),
        ('TAM', 'Tamaulipas'),
        ('TLA', 'Tlaxcala'),
        ('VER', 'Veracruz'),
        ('YUC', 'Yucatán'),
        ('ZAC', 'Zacatecas'),
    ]

    estado = models.CharField(max_length=3, choices=ESTADOS_MEXICO, default='CDX')


class Telefono (models.Model):
    TIPO_TEL = [
        (1,'CASA'),
        (2,'MOVIL'),
    ]
    tipo = models.IntegerField(choices=TIPO_TEL, default=1)
    alias = models.CharField(max_length=255)
    numero = models.CharField(max_length=50)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, related_name='telefonos')

