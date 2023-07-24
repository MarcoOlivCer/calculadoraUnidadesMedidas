from tkinter import*
from tkinter import ttk


#cores
#variavel que recebe a cor em hexadecimal
cor1 = '#3b3b3b' #preto ; black
cor2 = '#ffffff' #branco ; white
cor3 = '#b8d5d7' #azul claro ; blue


# config da janela
janela = Tk()
janela.title('Calculadora de Medidas')
janela.geometry('650x400')
janela.configure(bg=cor1)


#---------------------------------------frames para dividir a janela -------------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=53)

frame_direita = Frame(janela, width=198, height=310, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#---------------------------------------estilo das janela -------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#---------------------------------------Confirgurando Frame cima -------------------

l_app_nome = Label(frame_cima, text= 'Calculadora de Unidades de Medidas ', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

#---------------------------------------Configurando Frame Esquerda -------------------

b_0 = Button(frame_esquerda, text= 'Peso ', width=10, height=0 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 15 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)



janela.mainloop()