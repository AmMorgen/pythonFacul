#Receber o inteiro T
T = int(input())

#Verifico se T <= 100
#Nesse caso o que acontece se sim
if(T <= 100):
    saidas = []
    #faco um loop para cada teste determinado pelo usuario
    for t in range(0, T):
        #Recebo N
        N = int(input())
        #Verifico se N:(1<=N<=100)
        #Nesse caso o que acontece se sim
        if(N >= 1 and N <= 100):
            #crio um vetor/lista para receber as instrucoes 
            instrucoes = []
            #um loop para receber as N instrucoes do usuario
            for n in range(0, N):
                #recebo a instrucao atual
                instrucao = input()
                #verifico se ela e SAME AS i (ou seja nao eh igual a LEFT nem igual a RIGHT)
                if(instrucao != "LEFT" and instrucao != "RIGHT"):
                    #como nossos vetores comecao do 0 e o index de SAME AS i a partir do 1 eu tiro -1 do i
                    temp = ""
                    for c in range(8, len(instrucao)):
                        temp += instrucao[c]
                    i = int(temp) - 1
                    #o i de SAME AS i comeca a partir do index 8 na string de instrucao, ou seja faco um loop apenas para salvar 
                    #o numero i  e depois transforma-lo em um inteiro 
                    if(i < n):#Verifico se i eh uma instrucao anterior, se for maior ou igual nao.
                        instrucoes.append(instrucoes[i]) # praticamente same as i eh para repitir uma i-esima instrucao
                        #apenas readiciono essa instrucao no vetor/lista de instrucoes
                else:
                    #caso constrario ele eh so LEFT ou RIGHT
                    instrucoes.append(instrucao)
            #Agora que so tenho LEFT e RIGHT no vetor/lista instrucoes eu vou determinar a posicao e armazenar em saidas
            #comeca do 0 por que nao movimentei ainda
            posicao = 0
            for instrucao in instrucoes:
                #SE for LEFT tiro -1 da posicao
                if(instrucao == "LEFT"):
                    posicao -= 1
                else:
                    #caso constrario adiciono +1 na posicao
                    posicao += 1
            #mostro a posicao atual
            saidas.append(posicao)
    for saida in saidas:
        print(saida)