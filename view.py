# importando SQLite
import sqlite3 as lite

#CRUD - CREATE/READ/UPDATE/DELETE

#criando conexao 
con = lite.connect('dados.db')

#CREATE - INSERIR
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia, produto, assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)

#READ - LER/MOSTRAR
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall() #fetchall - pega tudo

        for i in informacao:
            lista.append(i)
    return lista

#UPDATE - ALTERAR/ATUALIZAR
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia=?, produto=?, assunto=? WHERE id=?"
        cur.execute(query, i)  

#DELETE - DELETAR/APAGAR
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)