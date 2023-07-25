from tkinter import*
from tkinter import ttk

from PIL import ImageTk, Image


#cores
#variavel que recebe a cor em hexadecimal
cor1 = '#3b3b3b' #preto ; black
cor2 = '#ffffff' #branco ; white
cor3 = '#b8d5d7' #azul claro ; blue


# config da janela
janela = Tk()
janela.title('Calculadora de Medidas')
janela.geometry('650x260')
janela.configure(bg=cor1)


#---------------------------------------frames para dividir a janela -------------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=53)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#---------------------------------------estilo das janela -------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#---------------------------------------Confirgurando Frame cima -------------------

l_app_nome = Label(frame_cima, text= 'Calculadora de Unidades de Medidas ', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

#---------------------------------------Configurando Frame Esquerda -------------------

img_0 = Image.open('Icons/weight.png')
img_0 = img_0.resize((40,40), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text= 'Peso', image=img_0, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

img_1 = Image.open('Icons/time.png')
img_1 = img_1.resize((40,40), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_0 = Button(frame_esquerda, text= 'Tempo', image=img_1, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

img_2 = Image.open('Icons/length.png')
img_2 = img_2.resize((40,40), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_0 = Button(frame_esquerda, text= 'Comprimento', image=img_2, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

img_3 = Image.open('Icons/quadrado.png')
img_3 = img_3.resize((40,40), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_0 = Button(frame_esquerda, text= 'Area', image=img_3, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

img_4 = Image.open('Icons/pluviometro.png')
img_4 = img_4.resize((40,40), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_0 = Button(frame_esquerda, text= 'Quantidade', image=img_4, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

img_5 = Image.open('Icons/speed.png')
img_5 = img_5.resize((40,40), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_0 = Button(frame_esquerda, text= 'Velocidade', image=img_5, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

img_6 = Image.open('Icons/temperature.png')
img_6 = img_6.resize((40,40), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_0 = Button(frame_esquerda, text= 'Temperatura', image=img_6, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

img_7 = Image.open('Icons/security-energy.png')
img_7 = img_7.resize((40,40), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_0 = Button(frame_esquerda, text= 'Energia', image=img_7, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

img_8 = Image.open('Icons/pressure.png')
img_8 = img_8.resize((40,40), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_0 = Button(frame_esquerda, text= 'Pressão', image=img_8, compound=LEFT, width=130, height=50 , relief='flat', overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)



janela.mainloop()