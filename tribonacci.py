N = int(input())

def tribonacci(n):
    if(n > 1):
        saida = [1,1]
        for i in range(2, n):
            soma = 0
            if(i == 2):
                soma += saida[0] + saida[1]
            else:
                soma += saida[i-1] + saida[i-2] + saida[i-3]
            saida.append(soma)
    else:
        saida = [1]
    return saida
    2
print(tribonacci(N))