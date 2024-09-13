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

def insert():
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
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            dia = cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            
            update_list = [nome, email, telefone, dia, estado, assunto, valor]

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
                
                for widgrt in rightFrame.winfo_children():
                    widget.destroy()
                show()
                
                
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela!')





janela.mainloop()