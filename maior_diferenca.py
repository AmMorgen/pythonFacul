N = int(input())
M = int(input())
matriz = []

for i in range(N):
    linha = []
    for j in range(M):
        aux = int(input())
        linha.append(aux)
    matriz.append(linha)

maior = matriz[0][0]

for i in range(N):
    for j in range(M):
        if(matriz[i][j] > maior):
            maior = matriz[i][j]

for i in range(N):
    for j in range(M):
        matriz[i][j] -= maior

print(matriz)