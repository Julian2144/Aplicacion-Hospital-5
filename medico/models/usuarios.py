from django.db import models
class Usuarios (models.Model):
    Id_usuario = models. CharField (primary_key=True,unique=True,max_length=50)
    Contraseña = models. CharField ('Contraseña',max_length=50)
    


