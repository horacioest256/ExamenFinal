from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class datosUsuario(models.Model):
    profesion = models.CharField(max_length=48, null=True, blank=True)
    nroCelular = models.CharField(max_length=16, null=True, blank=True)
    perfilUsuario = models.CharField(max_length=256, null=True, blank=True)
    usuarioRelacionado = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)

