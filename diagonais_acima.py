N = int(input())
matriz = []

media = 0
for i in range(N):
    temp = []
    for j in range(N):
        aux = int(input())
        media += aux
        temp.append(aux)
    matriz.append(temp)

media = media / (N * N)
soma = 0
for i in range(N):
    for j in range(i+1, N):
        soma += matriz[i][j]

abaixo_media = 0

for i in range(N):
    for j in range(N):
        if(matriz[i][j] < media):
            abaixo_media += 1

print("{}\n{}".format(soma, abaixo_media))