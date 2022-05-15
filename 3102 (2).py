N = int(input())

testes = []

def calculaDeterminante(elementos):
    return 

for i in range(N):
    testes.append(list(map(int, input().split())))

areas = []


for triangulo in testes:
    det = (((triangulo[0] * triangulo[3] * 1) + (triangulo[1] * 1 * triangulo[4]) + (1 * triangulo[2] * triangulo[5])) - ((triangulo[1] * triangulo[2] * 1) + (triangulo[0] * 1 * triangulo[5]) + (1 * triangulo[3] * triangulo[4])))
    if(det < 0):
        det *= (-1)
    areas.append(det * (1/2))


for area in areas:
    print('{:.3f}'.format(area))
