N = int(input())

media = 0
soma = 0
produto = 1
menor = 0
maior = 0
for i in range(0, N):
    entrada = int(input())
    soma += entrada
    produto *= entrada
    if(entrada < menor):
        menor = entrada
    if(entrada > maior):
        maior = entrada
    media = soma / N

print(media) 
print(soma)
print(produto)
print(menor)
print(maior)


