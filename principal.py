'''
------------------------UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARÁ--------------------------
COMPLEXIDADE DE ALGORITMOS                  ALGORITMO DA SUBSEQUÊNCIA COMUM MAIS LONGA - Aplicação com cadeias de DNA                 
Algoritmo de Programação Dinâmica           Classe principal para receber os valores e salvar em txt
Professor: Manoel Ribeiro 

Discentes:
1. Amanda Fiel Savino
2. Beatriz de Jesus Silva Cavalcante 
3. Manoel Malon Costa de Moura
'''
#fazendo a importação da função calcula_LCS do código Segmento Comum
from SegmentoComum import calcula_LCS

#nome correspondente do arquivo do resultado atual
resultado = "resultado.txt"

#nome correspondente do arquivo de todos os resultados
todosResultados = "todosResultados.txt"

#primeira cadeia de DNA digitada
cadeiaA = input("Digite a primeira sequência genética do DNA: ")

#segunda cadeia de DNA digitada
cadeiaB = input("Digite a segunda sequência do DNA: ")

#opt é a tabela utilizada & sequence é o resultado da comparação
opt, sequence = calcula_LCS(cadeiaA, cadeiaB)

n = len(cadeiaA)
m = len(cadeiaB)

#abrindo o arquivo txt do resultado local
arquivoSaida = open(resultado, "w")

#escritas no arquivo txt
arquivoSaida.write("\nPrimeiro DNA: " + cadeiaA)
arquivoSaida.write("\nSegundo DNA: " + cadeiaB)
arquivoSaida.write("\nTabela: \n\n")
arquivoSaida.write("  y ")

#escrita da palavra da cadeia B na matriz
for i in list(cadeiaB):
    arquivoSaida.write(i+" ")

arquivoSaida.write("\n")
arquivoSaida.write("x ")
k = 0

#escrita da matriz com os valores da cadeia A na primeira coluna
for i in range(0, n+1):
    if(i > 0):
        arquivoSaida.write(cadeiaA[k]+" ")
        k = k + 1
    for j in range(0, m+1):
        arquivoSaida.write(str(opt[i][j]) + " ")
    arquivoSaida.write("\n")

arquivoSaida.write("\nTamanho do resultada da Comparação: " + str(opt[n][m]))
arquivoSaida.write("\nResultado: " + sequence)

#abrindo o arquivo txt com todos os resultados
todasSaidas = open(todosResultados, 'a')

#abrindo o arquivo txt com o resultado local
arquivoSaida = open(resultado, 'r')

#lendo o arquivo local para impressão no terminal
todasSaidas.write("\n--------------------------------------------------------------")
for linha in arquivoSaida:
    print(linha)
    todasSaidas.write(linha)

todasSaidas.write("\n--------------------------------------------------------------")

#fechando os arquivos
todasSaidas.close()
arquivoSaida.close()
