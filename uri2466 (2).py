N = int(input())
M = list(map(int, input().split()))

linhas = []
linhas.append(M)

K = 1
for i in range(N - 1):
    novaLinha = []
    a, b = 0, 1
    for j in range(N - K):
        elemento = 0
        if(linhas[K-1][a] != linhas[K-1][b]):
            elemento = -1
        else:
            elemento = 1
        novaLinha.append(elemento)
        a+=1
        b+=1
    linhas.append(novaLinha)
    K+=1

if(linhas[-1][0] == 1):
    print("preta")
else:
    print("branca")