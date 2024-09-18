import sys
import sqlite3 as lite
from datetime import datetime

con = lite.connect('form.db')

lista = [['Yas Alves', 'yas@gmail.com', 12345678, '14/12/2020', 'Normal', 'Consulta presencialmente'],
         ['Maria Luiza', 'malu@gmail.com', 45678932, '05/10/2025', 'Normal', 'Consulta presencialmente'],
         ['João Futi', 'JF@gmail.com', 13266253, '19/12/2020', 'Normal', 'Consulta presencialmente'],
         ['Snyder Davi', 'SD@gmail.com', 56868661, '01/09/2020', 'Normal', 'Consulta presencialmente'],
         ['Suzi Gomes', 'SG@gmail.com', 11123652, '07/06/2020', 'Normal', 'Consulta presencialmente']]

#insert form
def inserir_form(i): # i é uma lista de valores que sera inserida no form
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Formulario(nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(query, i)      
        
#delete form
def deletar_form(i):
    
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Formulario WHERE id = ?'
        cur.execute(query, i)
        
#Update form

def atualizar_form(i):
    with con: 
        cur = con.cursor()
        query = 'UPDATE Formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?'
        cur.execute(query, i)        
        
#função que retorna todos os registros da tabela form
def selecionar_form():
    lista_form = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Formulario')
        rows = cur.fetchall() # recupera todas as linhas retornadas
        for row in rows: #laço for que adiciona cada linha(registro) na lista_form
            lista_form.append(row)
    return lista_form
listas = selecionar_form()