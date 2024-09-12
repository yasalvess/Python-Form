import sqlite3 as lite

con = lite.connect('form.db')

with con:
    #cria um cursor pra executar comandos SQL
    cur = con.cursor()
    cur.execute('CREATE TABLE Formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                + 'nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)')
    