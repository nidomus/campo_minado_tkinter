from cgitb import text
from email.mime import image
from tkinter import *
from setuptools import Command
import funcoes as cm
from tkinter import messagebox

#      Campo Minado IFBA (GUI)
# Linguagem de Programação 2022.1
#          :Autores:
#    EDNA DE OLIVEIRA DEGANI
#    FERNANDO PEREIRA FEITOZA
#  HERBERT FERNANDES DE OLIVEIRA
#      JONATHAN ROCCO GOMES 
# MARIA GABRIELA SANTANA PORTELA ERNESTO
#   NICKSON CAIRO SANTOS RIBEIRO

# Obs1.: A funcionalidade de Ranking não foi totalmente implementada
# Obs2.: Para adicionar uma bandeira clique com o botão direito
# Obs3.: Foram utilizadas as mesmas funções em ambas as versões

def iniciaJogo(tela,dificuldade,novo,lin,col,qtdBomb):

    if novo == True: # Essa estrutura serve para limpar os widgets quando um novo jogo é iniciado, evitando a sobreposição de campos
        for filho in tela.winfo_children()[1:3]: # Percorre todos os widgets 'filhos' da aplicação principal, evitando o Menu.
            filho.destroy() # Destrói os widgets

   
    tela.config(bg='green')
    zona_topo = Frame(tela, bg='red', bd=5)
    zona_topo.grid(row=0, pady=(5))

    zona_campo = Frame(tela)
    zona_campo.grid(row=1)
    
    if dificuldade ==0:
        proporcao = '50x50'
    if dificuldade ==1:
        proporcao = '30x30'
    if dificuldade ==2:
        proporcao = '25x25'

    campo = PhotoImage(file=f'imagens/{proporcao}/campo.png')
    vazio = PhotoImage(file=f'imagens/{proporcao}/vazio.png')
    valor1 = PhotoImage(file=f'imagens/{proporcao}/valor1.png')
    valor2 = PhotoImage(file=f'imagens/{proporcao}/valor2.png')
    valor3 = PhotoImage(file=f'imagens/{proporcao}/valor3.png')
    valor4 = PhotoImage(file=f'imagens/{proporcao}/valor4.png')
    valor5 = PhotoImage(file=f'imagens/{proporcao}/valor5.png')
    mina = PhotoImage(file=f'imagens/{proporcao}/mina.png')
    bandeira = PhotoImage(file =f'imagens/{proporcao}/bandeira.png')

    qtdLinhas = lin
    qtdColunas = col
    qtdBombas = qtdBomb
    qtdBandeiras = StringVar()
    qtdBandeiras.set(qtdBombas)
    qtdJogadas = StringVar()
    qtdJogadas.set(0)
    matriz_botoes = []

    with open("Ranking.txt",'r') as arquivo:
        ranking = arquivo.readlines()
    
    for item in ranking:
        print(item)    

    matriz = cm.gerarMatriz(qtdLinhas,qtdColunas, 0).copy()
    tabuleiro = cm.gerarMatriz(qtdLinhas,qtdColunas, -3)
    cm.sorteioBomba(matriz, qtdLinhas,qtdColunas, qtdBombas)
    cm.contBombas(matriz, qtdLinhas,qtdColunas)
    # app.configure(bg='grey')

    # Parte superior do jogo
    label_texto_bandeira = Label(zona_topo,text='Bandeiras: ',font=30)
    label_texto_bandeira.grid(row= 0,column= 0)
    label_bandeiras = Label(zona_topo, textvariable=qtdBandeiras, font= 30)
    label_bandeiras.grid(row = 0, column=1)

    label_texto_jogadas = Label(zona_topo,text='Jogadas: ',font=30)
    label_texto_jogadas.grid(row= 0,column= 2)
    label_jogadas = Label(zona_topo, textvariable=qtdJogadas, font= 30)
    label_jogadas.grid(row = 0, column=3)

    # Inicializa a matriz de botões
    for l in range(qtdLinhas):
        aux_botoes = []
        for c in range(qtdColunas):
            aux_botoes.append(Button(zona_campo, image=campo,bd=0,relief=SUNKEN, text=f'{l}{c}'))
        matriz_botoes.append(aux_botoes)

    # adiciona os botões na tela com o grid
    for l in range(qtdLinhas):
        for c in range(qtdColunas):
            matriz_botoes[l][c].grid(row=l, column=c)

    #atribui uma função para cada clique do mouse sobre o botão (jogada, bandeira)
            matriz_botoes[l][c].bind('<Button-1>', lambda event, linha=l, coluna=c: clique_esquerdo(linha, coluna))
            matriz_botoes[l][c].bind('<Button-3>', lambda event, linha=l, coluna=c: clique_direito(linha, coluna))

    def clique_esquerdo(lin, col):
            flag = False
            if matriz[lin][col] == 0:
                flag = True
            if str(matriz_botoes[lin][col]['image']) != str(bandeira): # verifica se o jogador não marcou a casa com uma bandeira, caso contrario, a casa fica travada
                fimDeJogo = cm.jogadas(matriz, tabuleiro, qtdLinhas,qtdColunas, lin, col)
                qtdJogadas.set(int(qtdJogadas.get())+1)
                bandeiras = 0 # guarda a quantidade de bandeiras que foram abertas sem bombas
                if fimDeJogo == False:
                    for l in range(qtdLinhas):
                        for c in range(qtdColunas):
                            if str(matriz_botoes[l][c]['image']) == str(bandeira) and tabuleiro[l][c] !=-3:
                                bandeiras +=1
                            if tabuleiro[l][c] == -2:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=vazio)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            if tabuleiro[l][c] == 1:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=valor1)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            if tabuleiro[l][c] == 2:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=valor2)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            if tabuleiro[l][c] == 3:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=valor3)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            if tabuleiro[l][c] == 4:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=valor4)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            if tabuleiro[l][c] == 5:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=valor5)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')

                    qtdBandeiras.set(int(qtdBandeiras.get())+bandeiras) # retorna as bandeiras encontradas na abertura de casas para o total
                    if cm.verificarVitoria(tabuleiro,qtdBombas,qtdLinhas,qtdColunas):
                        matriz.clear()
                        mostrarPontuacao(tela)
                else:
                    for l in range(qtdLinhas):
                        for c in range(qtdColunas):
                            if matriz[l][c] == -1:
                                matriz_botoes[l][c].configure(activebackground='white',bg='white',image=mina)
                                matriz_botoes[l][c].unbind('<Button-1>') # remove os comandos do widget para bloquear a ação
                                matriz_botoes[l][c].unbind('<Button-3>')
                            # else:
                            #     matriz_botoes[l][c].destroy()
                            #     matriz_botoes[l][c]=Label(janela,image=campo)
                            #     matriz_botoes[l][c].grid(row=l,column=c)

                    msg = ('Ops!','Você perdeu!')
                    popup(msg)

    def clique_direito(l, c):
        if str(matriz_botoes[l][c]['image']) != str(bandeira):
            if int(qtdBandeiras.get())>0:
                matriz_botoes[l][c].configure(image=bandeira)
                qtdBandeiras.set(int(qtdBandeiras.get())-1)
        else:
            matriz_botoes[l][c].configure(image=campo)
            qtdBandeiras.set(int(qtdBandeiras.get())+1)
    def mostrarPontuacao(app):
        janela = Toplevel(app)
        janela.grid()
        janela.resizable(0,0)
        janela.title('Pontuação')
        janela.geometry('200x150')
        janela.grab_set()
        tela.eval(f'tk::PlaceWindow {str(janela)} center')
        label_msgV = Label(janela, text=f'Parabéns!\n Você concluiu o Campo Minado\n com {qtdJogadas.get()} jogadas.')
        label_msgV.pack()
        label_nome = Label(janela, text='Nome do jogador')
        label_nome.pack(padx=10)

        nomeJogador = Entry(janela)
        nomeJogador.pack()
        btn_salvar = Button(janela,text='Salvar',command= lambda:[guardarPontuacao(janela,nomeJogador.get(),qtdJogadas.get())])
        btn_salvar.pack()

    def guardarPontuacao(janela,nome,pontuacao):
        # janela.destroy()

        # ranking.append(nome+':'+pontuacao)
        # for item in ranking:
        #     for x in item:


        # arquivo = open('Ranking.txt','w')
        # arquivo.write(ranking)
        # arquivo.write(':'+pontuacao)"
        
        pass
        
    def popup(texto):
        aviso = messagebox.askyesno(f'{texto[0]}',f'{texto[1]}\nQuer jogar novamente?')
        if aviso == 1:
            iniciaJogo(app,dificuldade,True,qtdLinhas,qtdColunas,qtdBomb)
        else:
            tela.quit()

def novoJogoFacil():
    iniciaJogo(app,0,True,8,10,10)

def novoJogoMedio():
    iniciaJogo(app,1,True,14,18,40)

def novoJogoDificil():
    iniciaJogo(app,2,True,20,24,99)

def novoJogoCustom():
    jogo_customizado = Toplevel(app)
    jogo_customizado.grid()
    jogo_customizado.resizable(0,0)
    jogo_customizado.title('Jogo Customizado')
    jogo_customizado.geometry('200x100')
    jogo_customizado.grab_set()
    app.eval(f'tk::PlaceWindow {str(jogo_customizado)} center')
    label_linha = Label (jogo_customizado, text='Linha: ')
    label_linha.pack()
    label_linha = Label (jogo_customizado, text='Linha: ')
    label_linha.pack()
    

app = Tk()


menuBar = Menu(app)
menuJogo = Menu(menuBar, tearoff=0)
menuJogo.add_command(label='Fácil (8x8, 10 bombas)', command= novoJogoFacil)
menuJogo.add_command(label='Médio (9x9, 20 bombas)', command= novoJogoMedio)
menuJogo.add_command(label='Difícil (10x10, 30 bombas)', command = novoJogoDificil)
menuJogo.add_command(label='Customizado', command = novoJogoCustom)

menuBar.add_cascade(label='Novo Jogo', menu=menuJogo)

app.config(menu = menuBar)
app.title('CAMPO MINADO')
iniciaJogo(app,0,False,8,10,10)
app.eval('tk::PlaceWindow . center')
app.iconbitmap('imagens/CM.ico')

app.resizable(0,0)
app.mainloop()
