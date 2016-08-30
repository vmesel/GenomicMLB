import sys
import os
import random

def baserandomica():
	bases = ["A", "C", "T", "G"]
	return random.choice(bases)
	
def gerasequencia(length):
	sequencia = []
	length = int(length) - 1
	for i in range(length):
		sequencia.append(baserandomica())
	return "".join(sequencia)

def gerasequenciacompadrao(length, padrao):
	_pdr_tam = len(padrao)
	_len_seq_sp = int(length) - int(_pdr_tam)
	_separador = random.randint(0, _len_seq_sp)
	
	_seqa = gerasequencia(_separador)
	_seqb_valor = length - _pdr_tam - _separador
	_seqb = gerasequencia(_seqb_valor)
	
	return _seqa + padrao + _seqb
	
def geratuplas(sequencias, length, padrao):
	#TODO: Implement a pattern list reader, for generating more patterns at once
	_seqlist = []
	for i in range(sequencias - 1):
		_seqlist.append(random.randint(0,1))
	
	outputs = []
	for i in _seqlist:
		if i == 0:
			outputs.append(gerasequencia(length))
		else:
			outputs.append(gerasequenciacompadrao(length, padrao))

	return zip(_seqlist, outputs)

def gerafasta(sequencias, length, padrao, fasta):
	_tuples = geratuplas(sequencias, length, padrao)

	f = open(fasta, "r+")	

	for item in _tuples:
		tipo, valor = item
		if tipo == 0:
			f.write(">seq_sem_padrao:RANDOM\n")
			f.write(valor + "\n")
		else:
			f.write(">seq_com_padrao:RANDOMCPADRAO\n")
			f.write(valor + "\n")
	return True

print(gerafasta(10, 32, "PADRAOAQUI", "fasta-out.fasta"))
