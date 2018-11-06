# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):

	id_login = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	fathor_rh = models.CharField(max_length=3)
	senha = models.CharField(max_length=30)
	nome = models.CharField(max_length=60)
	data_nasc = models.DateField(auto_now=False, auto_now_add=False)
	peso = models.FloatField()
	altura = models.FloatField()
	email = models.EmailField(max_length=100)
	sexo = models.CharField(max_length=1)
	tipo_sangue = models.CharField(max_length=2)

	def __str__(self):
	    return self.title

class Doacao(models.Model):

	id_doacao = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	data = models.DateField(auto_now=False, auto_now_add=False)
	medula = models.CharField(max_length=1)
	legenda = models.TextField()

	def __str__(self):
		return self.title

class Hemocentro(models.Model):
	
	id_hemocentro = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	horario = models.DateTimeField(blank=True, null=True)
	cidade = models.CharField(max_length=40)
	estado = models.CharField(max_length=15)
	rua = models.CharField(max_length=50)
	numero = models.CharField(max_length=6)
	bairro = models.CharField(max_length=30)
	complemento = models.CharField(max_length=15)
	cep = models.IntegerField()

	def __str__(self):
		return self.title

class Requisicao(models.Model):

	id_requisicao = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	data = models.DateField(auto_now=False, auto_now_add=False)
	tipo_sangue = models.CharField(max_length=2)
	fator_rh = models.CharField(max_length=3)

	def __str__(self):
		return self.title

