# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class UsuarioList(generics.ListCreateAPIView):

	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class DoacaoList(generics.ListCreateAPIView):

	queryset = Doacao.objects.all()
	serializer_class = DoacaoSerializer

class HemocentroList(generics.ListCreateAPIView):

	queryset = Hemocentro.objects.all()
	serializer_class = HemocentroSerializer

class RequisicaoList(generics.ListCreateAPIView):

	queryset = Requisicao.objects.all()
	serializer_class = RequisicaoSerializer

