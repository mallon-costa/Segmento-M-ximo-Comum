'''
------------------------UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARÁ--------------------------
COMPLEXIDADE DE ALGORITMOS                  ALGORITMO DA SUBSEQUÊNCIA COMUM MAIS LONGA - Aplicação com cadeias de DNA                 
Algoritmo de Programação Dinâmica			Classe contendo ao função responsável pelo o cálculo 
Professor: Manoel Ribeiro 


Discentes:
1. Amanda Fiel Savino
2. Beatriz de Jesus Silva Cavalcante 
3. Manoel Malon Costa de Moura
'''

import numpy as np


def calcula_LCS(A, B):
	n = len(A)
	m = len(B)

	# Opt array para armazenar o valor da solução ótima até a posição ith e jth para 2 strings
	opt = [[0 for i in range(0, m+1)] for j in range(0, n+1)]

	# Pi array para armazenar a direção ao calcular a sequência real
	pi = [[0 for i in range(0, m+1)] for j in range(0, n+1)]

	# Algoritmo para calcular o comprimento da subsequência comum mais longa
	for i in range(1, n+1):
		for j in range(1, m+1):
			if A[i-1] == B[j-1]:
				opt[i][j] = opt[i-1][j-1] + 1
				pi[i][j] = 0
			elif opt[i][j-1] >= opt[i-1][j]:
				opt[i][j] = opt[i][j-1]
				pi[i][j] = 1
			else:
				opt[i][j] = opt[i-1][j]
				pi[i][j] = 2
	# O comprimento da subsequência comum mais longa é salvo em opt[n][m]
	
	# Algoritmo para calcular a subsequência comum mais longa usando a matriz Pi
	i = n
	j = m
	S = ''

	while i>0 and j>0:
		if pi[i][j] == 0:
			S = A[i-1] + S
			i-=1
			j-=1
		elif pi[i][j] == 2:
			i-=1
		else:
			j-=1
    
	return opt,S
