import random as r


#      Campo Minado IFBA
# Linguagem de Programação 2022.1
#          :Autores:
#    EDNA DE OLIVEIRA DEGANI
#    FERNANDO PEREIRA FEITOZA
#  HERBERT FERNANDES DE OLIVEIRA
#      JONATHAN ROCCO GOMES 
# MARIA GABRIELA SANTANA PORTELA ERNESTO
#   NICKSON CAIRO SANTOS RIBEIRO


def gerarMatriz(lin,col,valor):
    # A função gerarMatriz() recebe como parâmetro o tamanho da matriz e o valor que será utilizado para preencher a mesma.
    # A função retorna uma matriz gerada.
    matriz = []
    for i in range(lin):
        lst = []
        for j in range(col):
            lst.append(valor)
        matriz.append(lst)
    return matriz

def verificarVitoria(matrizB,qtdBombas,lin,col):
    # A função recebe uma Matriz, a quantidade de bombas e o tamanho do jogo.
    tam = lin*col
    cont = 0 # contador de casas abertas para verificar a vitória do jogador
    totalCasas = (tam)-qtdBombas # guarda o total de casas do jogo menos a quantidade de bombas.
    #O totalCasas indica quantas casas (sendo elas vazias ou com os valores de bomba ao redor) o jogador deve abrir para vencer o jogo.
    for linha in range(lin):
        for coluna in range(col):
            if matrizB[linha][coluna] != -3: 
            # Se o espaço não for fechado, será somado +1 no contator
                cont +=1
        #Por outro lado, se a posição conter -3, significa que o jogador ainda não abriu a casa ou a mesma é uma bomba.
    if cont == totalCasas: 
    # Se o contador de casas abertas for igual o valor de totalCasas a função retornará True, indicando a vitória.
        return True

    return False # Se o código não entrar no if anterior significa que o jogador ainda não ganhou, e o retorno é False.

def exibirMatriz(m,lin,col): 
    # A função recebe uma matriz 'm' e o tamanho do jogo.
    # A fução exibe essa matriz seguindo regras de identificação para definir os ícones das casas.
    print(' ' , end=' ') # Espaçamento (Organização)
    
    for i in range(col):# Laço usado para imprimir os valores 
        print(i, end=' ')
    
    print()
    
    for linha in range(lin):
        print(linha, end=' ')
        for coluna in range(col):
            if m[linha][coluna]!=-1 and m[linha][coluna]!=-2 and m[linha][coluna]!=-3:
             # se a posição da matriz não conter -1 (bomba) e -2(percorrido), imprime o valor de bombas ao redor da casa
                print(m[linha][coluna], end=' ')
            elif m[linha][coluna]==-2:  # se a posição da matriz conter -2, imprime um espaço vazio (aberto)
                print(" ",end=" ")
            elif m[linha][coluna]==-3:  # se a posição da matriz conter -3, imprime um espaço fechado.
                print("◘",end=" ")
            else: # Se não for nenhuma das opções anteriores, imprime o ícone que representa a mina.
                print('☼',end=' ')
        print()

def confereQtdBombas(matriz,i,j,lin,col): # *Exclusivo do GUI*
    #Essa função busca deixar as bombas mais espalhadas no campo
    #Ainda está sendo testada
    cont=0
    for linha in range(i-1,i+2):
        for coluna in range(j-1,j+2):# 2 for's: fazer o giro nas casas ao redor (3x3)
            if(linha>=0 and linha<lin and coluna>=0 and coluna<col):
                if matriz[linha][coluna] == -1:
                    cont+=1
    return cont

def sorteioBomba(matriz,lin,col,qtdBombas):
    cont = 0
    while cont < qtdBombas:
        linha = r.randint(0, lin-1)  # i = linha / sortear as bombas
        coluna = r.randint(0, col-1)  # j = coluna

        if matriz[linha][coluna] == 0 and confereQtdBombas(matriz, linha,coluna,lin,col)<4:  # onde o lugar não tiver bomba, é inserida uma.
            matriz[linha][coluna] = -1
            cont += 1

def contBombas(matriz, lin,col):
    # A função contBomba recebe como parâmetro uma matriz ('zerada') e o tamanho do jogo (8x8,9x9,10x10)
    # A função percorre a matriz indicada buscando as casas que possuem bombas, e adiciona +1 ao redor das casas.
    # Dessa forma todas as casas que não são bombas serão preenchidas com o valor exato de bombas ao seu redor.
    # Se a casa continuar com valor zerado após a chamada dessa função, tal casa não possui bomba ao seu redor.

    for linha in range(lin):  # A estrutura dos For's (linha/coluna) percorre a matriz de ordem tam x tam.
        for coluna in range(col):  
            if matriz[linha][coluna] == -1:

                if linha == 0 and coluna == 0:  # verifica se a situação é do canto superior esquerdo
                    for l in range(linha, linha + 2):
                        for c in range(coluna, coluna + 2):
                            if matriz[l][c] != -1:  # percorre as linhas 2x2 (centro)
                                matriz[l][c] += 1

                elif linha == lin - 1 and coluna == 0:  # verifica se a situação é do canto inferior esquerdo
                    for l in range(linha - 1, linha + 1):
                        for c in range(coluna, coluna + 2):
                            if matriz[l][c] != -1:  # Matriz do canto inferior esquerdo (2x2)
                                matriz[l][c] += 1

                elif linha == lin - 1 and coluna == col - 1:  # verifica se a situação é do canto inferior direito
                    for l in range(linha - 1, linha + 1):
                        for c in range(coluna - 1, coluna + 1):
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                elif linha == 0 and coluna == col - 1:  # verifica se a situação é do canto superior direito
                    for l in range(linha, linha + 2):
                        for c in range(coluna - 1, coluna + 1):
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                elif linha == 0:  # verifica borda superior
                    for l in range(linha, linha + 2):  # percorre as linhas 3x2 (borda superior)
                        for c in range(coluna - 1, coluna + 2):  # percorre as colunas 3x2 (borda superior)
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                elif linha == lin - 1:  # verifica borda inferior
                    for l in range(linha - 1, linha + 1):  # percorre as linhas 3x2 (borda inferior)
                        for c in range(coluna - 1, coluna + 2):  # percorre as colunas 3x2 (borda inferior)
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                elif coluna == col - 1:  # verifica borda direita
                    for l in range(linha - 1, linha + 2):
                        for c in range(coluna - 1, coluna + 1):
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                elif coluna == 0:  # verifica borda esquerda
                    for l in range(linha - 1, linha + 2):
                        for c in range(coluna, coluna + 2):
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

                else:  # verifica a situação da posição (canto, centro, borda)
                    # Contando bomba
                    for l in range(linha - 1, linha + 2):  # percorre as linhas 3x3 (centro)
                        for c in range(coluna - 1, coluna + 2):  # percorre as colunas 3x3 (centro)
                            if matriz[l][c] != -1:
                                matriz[l][c] += 1

def abrirCasas(tabuleiro,matrizB,i,j,lin,col): 
  # A função abrir casas recebe como parâmetros uma matriz tabuleiro (revelada ao jogador), uma matriz com a lógica,
  # a coordenada da jogada (indicadas por i e j) e o tamanho do jogo.
  # A função irá percorrer as casas ao redor da coordenada passada em busca de casas que não sejam bomba para revelar ao jogador.
  # Caso seja encontrado mais uma casa com o valor 0 (vazio não percorrido), a função é chamada novamente passando, agora, as coordenadas
  # da posição do espaço encontrado.
  # Por recursão, esse processo irá repetir até que não seja maris encontrado casas vazias adjacentes.
  # Nessa condição, a função retornará ao ponto de origem, abrindo as casas restantes em cada chamada da função.

  matrizB[i][j] = -2 # Primeiramente, o valor da coordenada passada é alterada para -2, com o objetivo de evitar o loop infinito na recursão*
  
  #* O erro ocorre pois o valor de origem não é alterado e a função chamada por recursão encontra o valor 0 de origem, 
  # chamando novamente a função, sem progredir nas casas restantes.

  for linha in range(i-1,i+2):
    for coluna in range(j-1,j+2):# 2 for's: fazer o giro nas casas ao redor (3x3)
      if(linha>=0 and linha<lin and coluna>=0 and coluna<col): # verifica os casos impossíveis
        if matrizB[linha][coluna] !=-1:     #Se não for bomba, ele vai mostrar o que tem perto, revelando as casas na matriz tabuleiro.
          tabuleiro[linha][coluna] = matrizB[linha][coluna]
        if matrizB[linha][coluna] == 0:     #Verifica se tem mais casas vazias ao redor.
          abrirCasas(tabuleiro,matrizB,linha,coluna,lin,col) # A função abrirCasas(...) é chamada passando as coordenadas do valor 0 encontrado

def jogadas(matrizB,tabuleiro,qtdlin,qtdcol,i,j):
    # A função jogadas(...) recebe como parâmetro uma matriz (com a lógica), uma matriz tabuleiro (revelada ao jogador),
    # o tamanho do jogo e a coordenada da jogada ( l = linha e c = coluna ) 
    # A função possui um retorno booleano.
    # Ela retorna False se a jogada não cair em uma situação de Fim de Jogo.
    # Caso o jogador acerte uma casa com o valor -1 (bomba), será retornado True, indicando o Fim do Jogo.

    if matrizB[i][j]==0:                
    #Se a jogada cair em uma posição com o valor 0 (vazio e não percorrido), a função abrirCasas(...) é chamada, 
    # passando a coordenada da jogada atual.
        abrirCasas(tabuleiro,matrizB, i, j, qtdlin,qtdcol) #Chama a funçao de abrir casas vazias

    elif matrizB[i][j]>0:# Se a casa for um valor maior que zero, o mesmo será revelado, sem abrir as adjacentes.
        tabuleiro[i][j] = matrizB[i][j]  #Revela a casa no tabuleiro
    
    elif matrizB[i][j] == -1: # Se a jogada cair em uma posição com o valor -1, todas as bombas são exibidas e o jogo acaba.
        for linha in range(qtdlin):
            for coluna in range(qtdcol):
                if matrizB[linha][coluna]==-1:
                    tabuleiro[linha][coluna]='☼'
        return True # A função retorna True, pois o jogo encerrou.
    return False # A função retorna False, pois o jogo pode continuar.