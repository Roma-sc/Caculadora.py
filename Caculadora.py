# import tkinter
from tkinter import *  # Importa a biblioteca tkinter para criar a interface gráfica
from tkinter import ttk  # Importa o módulo ttk para usar temas e estilos

# Definindo as cores
cor1 = "#1e1f1e"  # Cor do fundo da janela
cor2 = "#feffff"  # Cor do fundo da tela
cor3 = "#38576b"  # Cor dos botões
cor4 = "#eceff1"  # Cor dos botões quando pressionados
cor5 = "#FFAB40"  # Cor do botão de igual

# Janelas

janela = Tk()  # Janela principal
janela.title("Calculadora Simples")  # Título da janela
janela.geometry("235x310")  # Tamanho da janela
janela.config(bg=cor1)  # Cor de fundo da janela

# Cria um frame para a tela da calculadora
Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)  # Cria um frame para a tela da calculadora

# Cria um frame para o corpo da calculadora
Frame_corpo = Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1, column=0)  # Cria um frame para o corpo da calculadora


todos_valores = ''  # Variável global para armazenar os valores digitados

# Criando a tela de exibição
valor_texto = StringVar()

# Função para entrar os valores na tela da calculadora


def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Valor na Tela
    valor_texto.set(todos_valores)

# Função para calcular o resultado da expressão


def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

# Função para limpar a tela da calculadora


def Limpar_Tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set(todos_valores)


  # Variável para armazenar o texto a ser exibido
app_label = Label(Frame_tela, textvariable=valor_texto, width=16, heigh=2, padx=7,
                  relief=FLAT, anchor="e", justify="right", font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Criando botões
b_1 = Button(Frame_corpo, command=Limpar_Tela, text="C", width=11, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(Frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5,
             fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(Frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(Frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(Frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(Frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5,
             fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(Frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(Frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(Frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(Frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(Frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(Frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(Frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(Frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(Frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(Frame_corpo, command=lambda: entrar_valores(','), text=",", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(Frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()  # Inicia o loop principal da janela