def receberLista():
    N = int(input())
    saida = []
    for i in range(N):
        temp = int(input())
        saida.append(temp)
    return saida

def maiorSequencia(lista):
    if(len(lista) > 1):
        sequencias_tamanhos = []
        inicio, fim = 0, 1
        anterior = lista[inicio]
        while(inicio != len(lista)-1):
            if(anterior >= lista[fim]):
                anterior = lista[fim]
                fim+=1
            else:
                sequencias_tamanhos.append(fim-inicio)
                inicio += 1
                fim = inicio + 1
        
        maior = sequencias_tamanhos[0]
        for i in sequencias_tamanhos:
            if(i > maior):
                maior = i
        return maior
    else:
        return len(lista)



lista_recebida = receberLista()
print(maiorSequencia(lista_recebida))