# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Registros
from .forms import PostForm

def tabla(request):
    context = {}
    context['Registros'] = Registros.objects.all()[::-1]
    context['form'] = PostForm()
    return render(request, 'Tabla.html', context)

def post_new(request):
	compra = request.POST.get('compra')
	post_new = Registros(compra=compra)
	post_new.save()
	return redirect('index')

def delete(request, id):
	compra = Registros.objects.get(pk=id)
	compra.delete()
	return redirect('index')