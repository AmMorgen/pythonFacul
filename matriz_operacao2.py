from tempfile import TemporaryDirectory


N = int(input())

matriz_A = []

for i in range(N):
    temporariaLinha = []
    for j in range(N):
        num = int(input())
        temporariaLinha.append(num)
    matriz_A.append(temporariaLinha)


matriz_B = []
for i in range(N):
    temporariaLinha = []
    for j in range(N):
        temporariaLinha.append(0)
    matriz_B.append(temporariaLinha)

for i in range(N):
    for j in range(N):
        for k in range(N):
            matriz_B[i][j] += matriz_A[i][k] * matriz_A[k][j]

matriz_AT = []

for i in range(N):
    temporariaLinha = []
    for j in range(N):
        temporariaLinha.append(matriz_A[j][i])
    matriz_AT.append(temporariaLinha)

matriz_C = []

for i in range(N):
    temporariaLinha = []
    for j in range(N):
        num = matriz_B[i][j] + matriz_AT[i][j]
        temporariaLinha.append(num)
    matriz_C.append(temporariaLinha)

print(matriz_C)