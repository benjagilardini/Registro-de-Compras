# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registros(models.Model):
	fecha = models.DateTimeField('Fecha',auto_now=True)
	compra = models.CharField(max_length = 100)
