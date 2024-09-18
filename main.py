from tkinter import *
from tkinter import scrolledtext
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
#Tk cria a janela principal
#StringVar lida com valores de texto
#messagebox exibe mensagens de alerta
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

c00_black = '#f0f3f5'
c01_white = '#feffff'
c02_green = '#4fa882'
c03_value = '#38576b'
c04_letter = '#403d3d'
c05_profit = '#e06636'
c06_blue = '#038cfc'
c07_red = '#ef5350'
c08_green_2 = '#263238'
c09_green_3 = '#e9edf5'
#c010_darkgrey = '#2E2E2E'

#windows
janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=c09_green_3)
janela.resizable(width=FALSE, height=FALSE)

#------------------FRAMES------------------

#cria um frame na parte superior da janela
upFrame = Frame(janela, width=310, height=50, bg=c02_green, relief='flat',)
upFrame.grid(row=0, column=0)

#cria um frame na parte inferior da janela
downFrame = Frame(janela, width=310, height=403, bg=c01_white, relief='flat')
downFrame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

rightFrame = Frame(janela, width=588, height=403, bg=c01_white, relief='flat')
rightFrame.grid(row=0, column=1, rowspan=2, pady=0, padx=1, sticky=NSEW) #rowspan = se estende por 2 linhas

#cria um texto no frame superior
app_ = Label(upFrame, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=c02_green, fg=c01_white)
app_.place(x=10, y=20)

global tree 

def inserir():
    #captura os valores dos campos de texto
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    dia = cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()
    
    #todos os valores capturados são armazenados em uma lista
    insert_list = [nome, email, telefone, dia, estado, assunto]
    
    if e_nome.get()=='':
        messagebox.showerror('Erro', 'Preencha todos os campos!')
    else:
        inserir_form(insert_list)
        
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')
        
        #limpar campos, após a inserção
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
        #destroi todos os widgets no frame da direita 
        for widget in rightFrame.winfo_children():
            widget.destroy()
        #atualiza a interface com os novos datos
        show()

def atualizar():
    try:
        #>Atualizando os dados selecionados em uma treeview(widget do tkinter usado para exibir dados em forma de tabela)<
        #-----------------------------------------------------------------------------------
        #focus() é uma função que retorna o item atualmente selecionado na arvore de dados
        treev_dados = tree.focus() #atribui o resultado da função focus do obj tree a variavel treev_dados
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        #limpa o conteudo do campo de texto e especifica o inicio (0) e o dim (end) a ser limpado
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
        #insere o valor do item no campo de texto, treev_lista[1] é o valor do item que foi obtido anteriormente
        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_tel.insert(0, treev_lista[3])
        cal.insert(0, treev_lista[4])
        e_estado.insert(0, treev_lista[5])
        e_assunto.insert(0, treev_lista[6])
        
        def update():
            
            #obtem os valores dos campos de texto
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            dia = cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            
            #criar uma lista com os valores obtidos
            update_list = [nome, email, telefone, dia, estado, assunto, valor]

            #verifica se o campo está vazio
            if e_nome.get() == '':
                messagebox.showerror('Erro', 'Preencha todos os campos!')
            else:
                atualizar_form(update_list)
                
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')
                
                botao_confirmar.destroy()
                
                for widget in rightFrame.winfo_children():
                    widget.destroy()
                show()
        botao_confirmar = Button(downFrame, command=update, text='Confirmar', width=10, height=1, bg=c02_green, fg=c01_white, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=105, y=380)
                
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela!')
def delete():
    try:
        #tree é um obj que representa uma árvore de dados, focus() é uma função que retorna o item atualmente selecionado
        treev_dados = tree.focus() #obtem o item selecionado na árvore de dados
        treev_dicionario = tree.item(treev_dados) #obtém um dicionarios de informações do item selecionado
        treev_lista = treev_dicionario['values'] #obtém a lista de valores do item [values é uma chave do dicionario que contem a lista de valores do item]
        valor = treev_lista[0] #obtem o primeiro valor da lista
        
        deletar_form([valor]) #chama a função com o valor
        print(valor)
        
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')
        
        for widget in rightFrame.winfo_children(): #iterar sobre os widgets do frame
            widget.destroy()
            
        show()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela!')

#criando label no Frame de baixo
l_nome = Label(downFrame, text = 'Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter)
l_nome.place(x=10, y=10) #posicionando o label no frame
#criando campo de texto, Entry é um widget que permite o usuário digitar o texto
e_nome = Entry(downFrame, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

l_email = Label(downFrame, text = 'Email *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter)
l_email.place(x=10, y=70) #posicionando o label no frame
#criando campo de texto, Entry é um widget que permite o usuário digitar o texto
e_email = Entry(downFrame, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

l_tel = Label(downFrame, text = 'Telefone *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter)
l_tel.place(x=10, y=130) #posicionando o label no frame
#criando campo de texto, Entry é um widget que permite o usuário digitar o texto
e_tel = Entry(downFrame, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

l_cal = Label(downFrame, text = 'Data da consulta *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter)
l_cal.place(x=10, y=190) #posicionando o label no frame
#criando campo de texto, Entry é um widget que permite o usuário digitar o texto
cal = DateEntry(downFrame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024) #DateEntry fornece o calendário para selecionar uma data, year se refere ao ano inicial do calendárop
cal.place(x=15, y=220)

l_estado = Label(downFrame, text = 'Estado da consulta *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter) 
l_estado.place(x=160, y=190) #posicionando o label no frame
#criando campo de texto, Entry é um widget que permite o usuário digitar o texto
e_estado = Entry(downFrame, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)

l_assunto = Label(downFrame, text = 'Consulta sobre *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=c01_white, fg=c04_letter) 
l_assunto.place(x=10, y=260) #posicionando o label no frame
#cassunto campo de texto, Entry é um widget que permite o usuário digitar o texto
e_assunto = Entry(downFrame, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=290)

insert_button = Button(downFrame, command=inserir, text='Inserir', width=10, height=1, bg=c06_blue, fg=c01_white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
insert_button.place(x=15, y=340)


update_button = Button(downFrame, command=atualizar, text='Atualizar', width=10, height=1, bg=c02_green, fg=c01_white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
update_button.place(x=105, y=340)

delete_button = Button(downFrame, command=delete, text='Deletar', width=10, height=1, bg=c07_red, fg=c01_white, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
delete_button.place(x=190, y=340)

def show():

    #define uma lista de cabeçalho pra tabela
    list_header = ['ID', 'Nome',  'Email', 'Telefone', 'Data', 'Estado', 'Sobre']
    
    df_list = selecionar_form() #chama a função selecionar_form() para obter os dados do BD e armazenar na variavel df_list
    
    global tree
    
    #cria um widget de tabela chamado 'treeview' 
    tree = ttk.Treeview(rightFrame, selectmode='extended', #extended permite que o usuario selecione múltiplas linhas da tabela
                        columns=list_header, show='headings') #list_header define os cabeçalhos da tabela e headings mostra apenas os cabeçalhos da tabela, sem a coluna de índice
    
    #cria uma barra de rolagem vertical para a tabela
    vsb = ttk.Scrollbar(
                        rightFrame, orient='vertical', command=tree.yview)
    
    #cria uma barra de rolagem horizontal para a tabela
    hsb = ttk.Scrollbar(
        rightFrame, orient='horizontal', command=tree.xview
    )
    
    #configurando as tabelas para usar as barras de rolagem
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    
    tree.grid(column=0, row=0, sticky='nsew') #posiciona a tabel no Frame
    vsb.grid(column=1, row=0, sticky='ns') #Posiciona a barra de rolagem vertical no frame
    hsb.grid(column=0, row=1, sticky='ew') #Posiciona a barra de rolagem horizontal no frame
    rightFrame.grid_rowconfigure(0, weight=12) #configura a altura da tabela p ocupar todo o espaço disponível no frame
    
    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center'] #define uma lista dfe alinhamentos para as colunas da tabela
    h=[30, 170, 140, 100, 120, 50, 100] #define uma lista de alinhamentos para as colunas da tabelas
    n=0 #define uma variavel para iterar sobre as colunas das tabelas
    
    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER) #DEFINE O CABEÇALHO DA COLUNA
        
        tree.column(col, width=h[n], anchor=hd[n]) #define a largura e o alinhamento da coluna
        n+=1 
        
    for item in df_list:
        tree.insert('', 'end', values=item) #insere os dados na tabela
show()
    

janela.mainloop()