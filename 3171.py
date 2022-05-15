'''
  a  b  c  d
a[1, 1, 1, 0]
b[1, 1, 0, 1]
c[1, 0, 1, 0]
d[0, 1, 0, 1]

  a  b  c  d  e  f
a[1, 1, 0, 0, 0, 0]
b[1, 1, 1, 0, 0, 0]
c[0, 1, 1, 1, 0, 0]
d[0, 0, 1, 1, 0, 0]
e[0, 0, 0, 0, 1, 1]
f[0, 0, 0, 0, 1, 1]
'''


def BFS(matriz):
    fila = []
    visitados = []
    fila.append(0)
    visitados.append(0)

    while(fila):
        m = fila.pop()
        for i in range(0, len(matriz)):
            if(matriz[m][i] == 1):
                if(i not in visitados):
                    visitados.append(i)
                    fila.append(i)
    for i in range(0, len(visitados)):
        visitados[i] += 1
    return visitados


N, L = map(int, input().split())

caminhos = []
for i in range(0, L):
    x, y = map(int, input().split())
    temp = []
    temp.append(x)
    temp.append(y)
    caminhos.append(temp)

matriz_adj = []

for i in range(0, N):
    temp = []
    for j in range(0, N):
        if(i == j):
            temp.append(1)
        else:
            temp.append(0)
    matriz_adj.append(temp)
for c in caminhos:
    matriz_adj[(c[0] - 1)][(c[1] - 1)] = 1
    matriz_adj[(c[1] - 1)][(c[0] - 1)] = 1

resultado = BFS(matriz_adj)

if(len(resultado) == N):
    print("COMPLETO")
else:
    print("INCOMPLETO")