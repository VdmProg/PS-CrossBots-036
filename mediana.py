# Inicia um vetor vazio
vetor = []

mediana = 0

# Imprime 'Entrada' no terminal
print('Entrada:')

# Recebe dois vetores do usuário
for i in range(2):
    entrada = input()
    for x in entrada:
        # Impede ',' e ' ' entrar no vetor total
        if x != ' ' and x != ',':
            # Não permite repetição no vetor
            if vetor.count(int(x)) == 0:
                vetor.append(int(x))

# Ordenar o vetor
for i in range(len(vetor)):
    for ii in range(len(vetor)):
        if vetor[i] < vetor[ii]:
            aux = vetor[i]
            vetor[i] = vetor[ii]
            vetor[ii] = aux

centro = int(len(vetor) / 2)

if len(vetor) % 2 == 0:
    mediana = (vetor[centro] + vetor[centro - 1]) / 2
else:
    mediana = vetor[centro]

print(vetor)
print(mediana)
