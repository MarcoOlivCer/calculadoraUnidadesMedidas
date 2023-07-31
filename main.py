from tkinter import*
from tkinter import ttk

#biblioteca para tratar imagens que usei para tratar os icones
from PIL import ImageTk, Image


#cores
#variavel que recebe a cor em hexadecimal
cor1 = '#3b3b3b' #preto ; black
cor2 = '#ffffff' #branco ; white
cor3 = '#b8d5d7' #azul claro ; blue


# config da janela
janela = Tk()
janela.title('Me de Pai')
janela.geometry('650x260')
janela.configure(bg=cor1)


#---------------------------------------frames para dividir a janela -------------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=53)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#---------------------------------------estilo das janela -----------------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#---------------------------------------Confirgurando Frame cima -------------------

l_app_nome = Label(frame_cima, text= 'Conversor de Unidades de Medidas ', height=1, padx=0,
                   relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)


#---------------------------------------Configurando Frame Direira -------------------

#Criando o espaço onde fica unidade
l_unidade_nome = Label(frame_direita, text = 'Unidade',width = 16, height=2 , padx=0, 
                       relief='groove', anchor='center', font=('Ivy 15 bold'), 
                       bg=cor2, fg=cor3)
l_unidade_nome.place(x=-3, y=-1)

#Criando quadrado DE
l_de = Label(frame_direita, text = 'De', height=1 , padx=3, relief='groove', 
             anchor='center', font=('Ivy 9 bold'), bg=cor2, fg=cor3)
l_de.place(x=10, y=70)

#Criando a Combobox do de
c_de = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_de.place(x=36, y=70)

#Criando o quadrado do Para
l_para = Label(frame_direita, text = 'Para', height=1 , padx=3, relief='groove', 
               anchor='center', font=('Ivy 9 bold'), bg=cor2, fg=cor3)
l_para.place(x=95, y=70)

#Criando a Combobox do Para
c_para = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_para.place(x=133, y=70)

#---------------------------------------Confirgurando Funcionalidades -------------------

#dicionario para formulas das unidades que vamos utilizar
unidades = {'Massa': [{'mg':0.001}, {'g': 1}, {'kg':1000}, {'t':1000000}],
            'Tempo': [{'ms': 0.001}, {'s': 1}, {'min': 60}, {'h': 3600}, {'d':86400}],
            'Comprimento': [{'mm':0.001},{'cm':0.01},{'m': 1},{'km':1000}],
            'Area': [{'km/s': 1}],
            'Quantidade': [{'l': 1}, {'ml': 0.001}, {'kl': 1000}],
            'Velocidade': [{'km/s': 1}],
            'Temperatura': [{'km/s': 1}],
            'Energia': [{'km/s': 1}],
            'Pressão':[{'km/s': 1}]
            }

#percorrer o dicionario e enviar para o junbbox

def monstrar_menu(i):
    
    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)


    c_de['values'] = unidade_de
    c_para['values'] = unidade_para
    
 
    l_unidade_nome['text'] = i


    def calcular():
        
        # Obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        # Obtendo o numero
        numero_para_converter = float(e_numero.get())
        
        '''criar uma forma de calculo individual para cada unidade de medida pois esse abaixo não       
           não vai servir para codigo completo.           
        '''
                     
        if unidade_para(a) <= unidade_de.index(b):
            #verificando a posição das unidades para obter o valor de distancia
            distancia = unidade_para.index(b) - unidade_de.index(a)
            resultado = numero_para_converter * (10**distancia)
        
        #**********************************************************************************
        
                
        print(a, b, numero_para_converter)
        
        



    # criando label, botão, entrada
    # O espaço onde colocamos os valores, apertamos em calcular e o resultado
    
    l_info = Label(frame_direita, text = 'Digite o numero', width = 16, height=2, padx=3, 
                       pady=3, relief='flat', anchor='center', font=('Ivy 10 bold'), 
                       bg=cor2, fg=cor3)
    l_info.place(x=25, y=110)
    
    e_numero = Entry(frame_direita, width=10, font=('Ivy 14 bold'), justify='center', 
                     relief=SOLID,)
    e_numero.place(x=5, y=150)
    
    b_calcular = Button(frame_direita, text= 'Calcular', command=calcular, width=7, height=0,
                        relief='raised', overrelief='ridge', anchor='nw',
                        font=('Ivy 9 bold'), bg=cor3, fg=cor2)
    b_calcular.place(x=120, y=150)

    l_resultado = Label(frame_direita, text = '000000', width = 13, height=1,
                        relief='groove', anchor='center', font=('Ivy 12 bold'), 
                        bg=cor2, fg=cor3)
    l_resultado.place(x=30, y=190)
    
    
    #criar uma logica para o usuario não inserir texto apenas numero na entrada    
    

#---------------------------------------Configurando Frame Esquerda -----------------------

#Botão do Massa
img_0 = Image.open('Icons/weight.png')
img_0 = img_0.resize((40,40), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Massa'), text= 'Massa', image=img_0,
             compound=LEFT, width=130, height=50, relief='flat', overrelief='solid',
             anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

#Botão do Tempo
img_1 = Image.open('Icons/time.png')
img_1 = img_1.resize((40,40), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Tempo'), text= 'Tempo', image=img_1,
             compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', 
             anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

#Botão do Comprimento
img_2 = Image.open('Icons/length.png')
img_2 = img_2.resize((40,40), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Comprimento'),  text= 'Comprimento', 
             image=img_2, compound=LEFT, width=130, height=50 , relief='flat', 
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

#Botão da Area
img_3 = Image.open('Icons/quadrado.png')
img_3 = img_3.resize((40,40), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_0 = Button(frame_esquerda,command=lambda:monstrar_menu('Area'), text= 'Area', image=img_3,
             compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', 
             anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

#Botão da Quantidade
img_4 = Image.open('Icons/pluviometro.png')
img_4 = img_4.resize((40,40), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Quantidade'), text= 'Quantidade', 
             image=img_4, compound=LEFT, width=130, height=50, relief='flat', 
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

#Botão da Velocidade
img_5 = Image.open('Icons/speed.png')
img_5 = img_5.resize((40,40), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Velocidade'), text= 'Velocidade',
             image=img_5, compound=LEFT, width=130, height=50 , relief='flat', 
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

#Botão da Temperatura
img_6 = Image.open('Icons/temperature.png')
img_6 = img_6.resize((40,40), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Temperatura'), text= 'Temperatura',
             image=img_6, compound=LEFT, width=130, height=50 , relief='flat',
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), 
             bg=cor3, fg=cor2)
b_0.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

#Botão Energia
img_7 = Image.open('Icons/security-energy.png')
img_7 = img_7.resize((40,40), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Energia'), text= 'Energia',
             image=img_7, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

#Botão Pressão
img_8 = Image.open('Icons/pressure.png')
img_8 = img_8.resize((40,40), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_0 = Button(frame_esquerda, command=lambda:monstrar_menu('Pressão'), text= 'Pressão', 
             image=img_8, compound=LEFT, width=130, height=50 , relief='flat',
             overrelief='solid', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)








janela.mainloop()