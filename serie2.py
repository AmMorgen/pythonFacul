#Recebo o X do usuario
X = int(input())
#Já incluo o logo na soma
S = float(X)
#o numerador comeca com 3
termo_A = 3
#o denominador comeca com 7
termo_B = 7
#simplesmente inicializo 
sinal = 1
#aqui vou somar os 100 termos
for i in range(0, 99):
    #Realizamos uma soma de termo
    S += sinal * ((termo_A * X) / (termo_B))
    #Atualizamos os termos A e B
    #Soma 5 no termoA e 2 no termo B
    #temos tbm inversão de sinal
    termo_A += 5
    termo_B += 2
    sinal *= -1

print(S)
