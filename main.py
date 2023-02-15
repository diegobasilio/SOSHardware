#importando o Tkinter
from tkinter import *
from tkinter import font
from cgitb import text
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry


#importando view
from view import *

#Cores
black = "#f0f3f5"  # preto
white = "#feffff"  # branco
green = "#1bcc3b"  # verde
darkgray = "#403d3d"   #cinza escuro
blue = "#038cfc"   # azul
red = "#e31912"   # vermelho
skyblue = "#3d94db"   # céu azul 
azulado = "#1c2a40"

#Janela
janela = Tk()
janela.title("")
janela.geometry('1110x453')
janela.configure(background= azulado)
janela.resizable(width=False, height=False)

#Frames SOSHardaware
frame_cima = Frame(janela, width=310, height=50, bg=azulado, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=azulado, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=white, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#App Software
app_nome = Label(frame_cima, text="SOS Hardware", anchor=NW, font=('Arial', 20, 'bold'), bg=azulado, fg=white, relief='flat')
app_nome.place(x=50, y=10)

#Label's and Entry's
l_nome = Label(frame_baixo, text="Nome", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

l_email = Label(frame_baixo, text="Email", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

l_tel = Label(frame_baixo, text="Telefone", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

l_cal = Label(frame_baixo, text="Data do Reparo", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_cal.place(x=15, y=220)

l_produto = Label(frame_baixo, text="Produto", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_produto.place(x=160, y=190)
e_produto = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_produto.place(x=160, y=220)

l_assunto = Label(frame_baixo, text="Assunto", anchor=NW, font=('Ivy 13 bold'), bg=azulado, fg=white, relief='flat')
l_assunto.place(x=10, y=260)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=290)

#funcao inserir/cadastrar
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    produto = e_produto.get()
    assunto = e_assunto.get()

    lista = [nome, email, tel, dia, produto, assunto]


    if nome=='':
        messagebox.showerror('Erro', 'Cadastro Não Preenchido!')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Cadastro Realizado Com Sucesso!') 

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_produto.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

#funcao alterar
def alterar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_produto.delete(0, 'end')
        e_assunto.delete(0, 'end')
        

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_produto.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_tel.get()
            dia = e_cal.get()
            produto = e_produto.get()
            assunto = e_assunto.get()

            lista = [nome, email, tel, dia, produto, assunto, valor_id]

            if nome=='':
                messagebox.showerror('Erro', 'Usuário Não Selecionado!')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Dados Alterados Com Sucesso!') 

                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_produto.delete(0, 'end')
                e_assunto.delete(0, 'end')
                            
            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        b_confirmar = Button(frame_baixo,command=update, text="Confirmar", width=10, font=('Arial 10 bold'), bg=blue, fg=black, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)   

    except IndexError:
        messagebox.showerror('Erro', 'Usuário Não Selecionado!')

#funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values'] 

        valor_id = [tree_lista[0]]  

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso','Usuário deletado!')

        for widget in frame_direita.winfo_children():
                widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Usuário Não Selecionado!')

#Botões
b_cadastrar = Button(frame_baixo,command=inserir,text="Cadastrar", width=10, font=('Arial 10 bold'), bg=green, fg=black, relief='raised', overrelief='ridge')
b_cadastrar.place(x=15, y=340)

b_alterar = Button(frame_baixo, command=alterar,text="Alterar", width=10, font=('Arial 10 bold'), bg=blue, fg=black, relief='raised', overrelief='ridge')
b_alterar.place(x=110, y=340)   
 
b_deletar = Button(frame_baixo, command=deletar,text="Deletar", width=10, font=('Arial 10 bold'), bg=red, fg=black, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=340)

def mostrar():
    global tree

    lista = mostrar_info()

    tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Produto', 'Assunto']
    
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    #scrollbar vertical      
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    #scrollbar horizontal
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')   
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    
    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30, 150, 160, 100, 90, 115, 135]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()
janela.mainloop()
