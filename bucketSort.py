from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    vector = []
    while size > 0:
        vector.append(size)
        size-=1
    return vector
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    #ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]

def bucketSort(vector):

    def quickSort(vector, inicio, fim):
        if inicio < fim:
            piv = randint(inicio, fim)
            temp = vector[fim]
            vector[fim] = vector[piv]
            vector[piv] = temp

            p = particao(vector, inicio, fim)
            quickSort(vector, inicio, p - 1)
            quickSort(vector, p + 1, fim)

        return vector

    def particao(vector, inicio, fim):
        piv = randint(inicio, fim)

        vector[fim], vector[piv] = vector[piv], vector[fim]

        pivInd = inicio - 1
        for index in range(inicio, fim):
            if vector[index] < vector[fim]:
                pivInd = pivInd + 1
                vector[pivInd], vector[index] = vector[index], vector[pivInd]

        temp = vector[pivInd + 1]
        vector[pivInd + 1] = vector[fim]
        vector[fim] = temp

        return pivInd + 1


    maior = max(vector)

    tam = len(vector)

    size = maior/tam

    bucket = [[] for _ in range(tam)]

    for i in range(tam):
        j = int(vector[i]/size)
        if j != tam:
            bucket[j].append(vector[i])
        else:
            bucket[tam - 1].append(vector[i])

    for i in range(tam):
        quickSort(bucket[i],0,len(bucket[i])-1)

    ans = []


    for i in range(tam):
        ans = ans + bucket[i]

    return ans
            

listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
y2=[]
y3=[]

for i in range(len(x2)):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))


for i in range(len(x2)):
  y.append(timeit.timeit("bucketSort({})".format(listas[i]),setup="from __main__ import bucketSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


print(operacoes[:])

desenhaGrafico(x2,y,'Quantidade','Tempo', 'bucketSort')
