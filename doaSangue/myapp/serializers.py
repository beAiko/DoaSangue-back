from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = Usuario
		fields = '__all__'

class DoacaoSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = Doacao
		fields = '__all__'

class HemocentroSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = Hemocentro
		fields = '__all__'

class RequisicaoSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = Requisicao
		fields = '__all__'
