# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Registro_Compras.models import Registros

# Create your views here.

def tabla(request):
    context = {}
    context['Registros'] = Registros.objects.all()
    return render(request, 'Tabla.html', context)