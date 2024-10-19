def compara(array):
    for x in array:
        if x != '.':
            repet = array.count(x)
            if repet > 1:
                invalido()


def invalido():
    print('Tabuleiro inválido')
    exit()


# Desenha a matriz
def desenhaMatriz():
    for i in range(9):
        print('|', end=' ')
        for ii in range(9):
            if matriz[i][ii] == '.':
                print(' ', end='  ')
            else:
                print(matriz[i][ii], end='  ')
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
    for i in range(9):
        for ii in range(9):
            if matriz[i][ii] not in '123456789.':
                invalido()


def comparaLinhas():
    for i in range(9):
        linha = matriz[i]
        compara(linha)


def comparaColunas():
    for ii in range(9):
        coluna = []
        # For que junta os números a serem comparados
        for i in range(9):
            coluna.append(matriz[i][ii])
        # For que faz a comparação
        compara(coluna)


def comparaBlocos():
    for i in range(0, 9, 3):
        for ii in range(0, 9, 3):
            bloco = []
            for iii in range(3):
                for iiii in range(3):
                    bloco.append(matriz[i+iii][ii+iiii])
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
