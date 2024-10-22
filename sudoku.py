def compara(array):
    # Para cada valor do array recebido
    for x in array:
        # Se for diferente de '.' (vazio)
        if x != '.':
            # Conte quantas vezes ele se repete dentro do array
            repet = array.count(x)
            # Se houver repetição
            if repet > 1:
                invalido()


def invalido():
    print('Tabuleiro inválido')
    exit()


# Desenha a matriz
def desenhaMatriz():
    # Para cada linha
    for i in range(9):
        # Inicie ela com | sem quebrar a linha
        print('|', end=' ')
        # Para cada valor da linha
        for ii in range(9):
            # Se for equivalente a vazio
            if matriz[i][ii] == '.':
                # Digite vazio sem quebrar linha
                print(' ', end='  ')
            # Senão
            else:
                # Digite o valor e não quebre linha
                print(matriz[i][ii], end='  ')
        # Finalize a linha com |
        print('|\n')


# Recebe linhas do tabuleiro
def recebeLinhas():
    # Recebe uma entrada para cada linha
    for i in range(9):
        linha = input()
        # Indice da coluna do valor recebido
        coluna = 0
        # Percorre a input
        for ii in linha:
            # Se tamanho maior que o suportado
            if len(linha) > 18:
                # Entrada Inválida
                invalido()
            # Se o valor for diferente de espaço
            elif ii != ' ':
                # Coloque-o no tabuleiro
                matriz[i][coluna] = ii
                coluna += 1


def verificaEntrada():
    # Para cada linha do array
    for i in range(9):
        # Pegue o valor na coluna ii
        for ii in range(9):
            # Verifique se o valor é válido
            if matriz[i][ii] not in '123456789.':
                invalido()


def comparaLinhas():
    # Para cada linha
    for i in range(9):
        # Transforme essa linha num novo array
        linha = matriz[i]
        # Verifica repetição
        compara(linha)


def comparaColunas():
    # Para cada coluna
    for ii in range(9):
        coluna = []
        # Pegue todos os valores da coluna
        for i in range(9):
            # Coloque eles num array
            coluna.append(matriz[i][ii])
        # Verifica repetição
        compara(coluna)


def comparaBlocos():
    # Vá de 3 em 3 linhas
    for i in range(0, 9, 3):
        # E de 3 em 3 colunas
        for ii in range(0, 9, 3):
            bloco = []
            # Para cada linha dessas 3 linhas
            for iii in range(3):
                # E cada valor dessas linhas
                for iiii in range(3):
                    # Coloque eles numa matriz
                    bloco.append(matriz[i+iii][ii+iiii])
            # Verifica repetição
            compara(bloco)


# Cria a matriz
matriz = []
repet = 0
valido = True

# Adiciona 9 arrays na matriz
for i in range(9):
    matriz = matriz + [[' ']*9]

# Recebe as linhas
recebeLinhas()
# Verifica Entrada
verificaEntrada()
# Comparação das linhas
comparaLinhas()
# Comparação das colunas
comparaColunas()
# Comparação dos regiões
comparaBlocos()

desenhaMatriz()
print('Ta permitido o inicio do jogo')
