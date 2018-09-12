# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Registro_Compras.models import Registros

from .forms import PostForm
# Create your views here.

def tabla(request):
    context = {}
    context['Registros'] = Registros.objects.all()
    return render(request, 'Tabla.html', context)

def post_new(request):
        form = PostForm()
        return render(request, 'Tabla.html', {'form': form})