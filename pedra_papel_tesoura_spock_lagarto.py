jogadorUmScore = 0
jogadorDoisScore = 0
empates = 0

for i in range(0, 3):
    pUm = int(input())
    pDois = int(input())
    if(pUm == 0):
        if(pDois == 3 or pDois == 4):
            jogadorUmScore+=1
        elif(pDois == 0):
            empates += 1
        else:
            jogadorDoisScore += 1
    if(pUm == 1):
        if(pDois == 0 or pDois == 4):
            jogadorUmScore += 1
        elif(pDois == 1):
            empates += 1
        else:
            jogadorDoisScore += 1
    if(pUm == 2):
        if(pDois == 0 or pDois == 1):
            jogadorUmScore += 1
        elif(pDois == 2):
            empates += 1
        else:
            jogadorDoisScore += 1
    if(pUm == 3):
        if(pDois == 1 or pDois == 2):
            jogadorUmScore += 1
        elif(pDois == 3):
            empates += 1
        else:
            jogadorDoisScore += 1
    if(pUm == 4):
        if(pDois == 2 or pDois == 3):
            jogadorUmScore += 1
        elif(pDois == 4):
            empates += 1
        else:
            jogadorDoisScore += 1

print(jogadorUmScore)
print(jogadorDoisScore)
print(empates)
