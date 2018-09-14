# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registros(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	compra = models.CharField(max_length=100)
	archive = models.BooleanField(default=False)