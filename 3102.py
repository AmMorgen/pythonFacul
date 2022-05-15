N = int(input())

testes = []

def calculaDeterminante(elementos):
    return (((elementos[0] * elementos[3] * 1) + (elementos[1] * 1 * elementos[4]) + (1 * elementos[2] * elementos[5])) - ((elementos[1] * elementos[2] * 1) + (elementos[0] * 1 * elementos[5]) + (1 * elementos[3] * elementos[4])))

for i in range(N):
    testes.append(list(map(int, input().split())))

areas = []


for triangulo in testes:
    areas.append(calculaDeterminante(triangulo) * (1/2))


for area in areas:
    print('{:.3f}'.format(area))
