n = 4
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

def leibniz(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    else:
        soma = 0
        for j in range(n):
            nova_matriz = []
            for i in range(1, n):
                linha = []
                for k in range(n):
                    if k != j:
                        linha.append(matriz[i][k])
                nova_matriz.append(linha)
            sinal = (-1) ** j
            soma += matriz[0][j] * sinal * leibniz(nova_matriz)
        return soma

deta = leibniz(matriz)
print("O determinante da matriz é:",deta)