import math

total_A = int(input()) #Armazena a quantidade inicial de pokemons do Player A
total_B = int(input()) #  -- - -- - - -- - -- - - -- - - -- - --  -- Player B
anos = 0 #variavel que vai armazenar a quantidade de anos decorridos
while(total_A < total_B):#condicao para verificar se o jgdr B passou o jgdr A
    total_A += math.floor((total_A * 50)/100) #Crescimento de 50% em relacao a qnt inicial do jgdr A
    total_B += math.floor((total_B * 30)/100) #Crescimento de 30% em relacao a qnt inicial do jgdr B
    anos+=1 #incrementa em anos, pois o crescimento é de acordo com anos
print(anos)
