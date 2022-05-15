H = int(input())

def granizo(h):
    sequencia = []
    sequencia.append(h)
    anterior = h
    while(anterior != 1):
        n = 0
        if(anterior % 2 == 0):
            n = (1/2) * anterior   
        else:
            n = (3*anterior) + 1
        sequencia.append(n)
        anterior = n
    maior = sequencia[0]
    for i in sequencia:
        if(i > maior):
            maior = i
    return maior

print(granizo(H))