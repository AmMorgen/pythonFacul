N = int(input())
matriz = []

for i in range(N):
    temp = []
    for j in range(N):
        aux = int(input())
        temp.append(aux)
    matriz.append(temp)

i, j = 0, 0
k, l = 0, N-1
while(i < N):
    aux = matriz[i][j]
    matriz[i][j] = matriz[k][l]
    matriz[k][l] = aux

    j+=1
    i+=1
    k+=1
    l-=1

invertido = []

i = N - 1
while(i >= 0):
    invertido.append(matriz[0][i])
    i-=1
matriz[0] = invertido


print(matriz)