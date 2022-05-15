def receberLista():
    N = int(input())
    saida = []
    for i in range(N):
        temp = int(input())
        saida.append(temp)
    return saida

def maiorSequencia(lista):
    if(len(lista) > 1):
        maior_seq = 0
        for i in range(len(lista)):
            for j in range(len(lista)):
                if(lista[i] > lista[j] and (j - i) > maior_seq):
                    maior_seq = j - i
                elif(lista[i] < lista[j]):
                    break
        return maior_seq + 1
    else:
        return len(lista)


lista_recebida = receberLista()
print(maiorSequencia(lista_recebida))