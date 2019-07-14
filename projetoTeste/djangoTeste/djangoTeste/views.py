from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return render(request, 'index.html')

def articles(request, year):
	return HttpResponse("O Ano informado foi : " + str(year))

def lerNomes(nome):
	listaNames = [{'nome':'Ana', 'idade':20},
				   {'nome':'Pedro', 'idade':25},
				   {'nome':'Joaquim', 'idade':27}]
	for pessoa in listaNames:
		if pessoa['nome'] == nome:
			return pessoa
	else:
		return {'nome': 'Não encontrado', 'idade':0}

def fname(request, nome):
	return HttpResponse(str(lerNomes(nome)['idade']))

def fname2(request, nome):
	getIdade = lerNomes(nome)['idade']
	return render(request, 'pessoa.html', {'getPessoa' : getIdade})