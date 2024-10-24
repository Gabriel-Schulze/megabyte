from customtkinter import *
from tkinter import Frame

class CadastroUsuario:
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Cadastro de Usuario")
        self.root.geometry('600x400+300+80')

        self.createWidget()

    def createWidget(self):


        CTkLabel(self.root,text="",  width=200,height=100).grid(column=0,row=0)

        CTkLabel(self.root, text="Nome:", font=("Open Sans",26)).grid(column=1,row=1)
        CTkLabel(self.root, text="CPF:", font=("Open Sans",26)).grid(column=1,row=2)
        CTkLabel(self.root, text="Telefone:", font=("Open Sans",26)).grid(column=1,row=3)
        CTkLabel(self.root, text="Email:", font=("Open Sans",26)).grid(column=1,row=4)
        CTkLabel(self.root, text="Senha:", font=("Open Sans",26)).grid(column=1,row=5)

        self.nome_entry = CTkEntry(self.root,font=("Open Sans",26),width=250)
        self.nome_entry.grid(column=2,row=1)

        self.cpf_entry = CTkEntry(self.root,font=("Open Sans",26),width=250)
        self.cpf_entry.grid(column=2,row=2)

        self.telefone_entry = CTkEntry(self.root,font=("Open Sans",26),width=250)
        self.telefone_entry.grid(column=2,row=3)

        self.email_entry = CTkEntry(self.root,font=("Open Sans",26),width=250)
        self.email_entry.grid(column=2,row=4)

        self.senha_entry = CTkEntry(self.root,font=("Open Sans",26),width=250)
        self.senha_entry.grid(column=2,row=5)

        self.btn_voltar = CTkButton(self.root, text="Voltar ao menu", width=10,command=self.voltarAoMenu, )
        self.btn_voltar.grid(column=1,row=6, pady=10)

        self.btn_cadastrar = CTkButton(self.root, text="Cadastrar",width=10 ,command=self.cadastrarUsuario)
        self.btn_cadastrar.grid(column=2,row=6, sticky=E)

    def voltarAoMenu(self):
        pass

    def cadastrarUsuario(self):
        pass

if __name__ == "__main__":
    root = CTk()
    app = CadastroUsuario(root)
    root.mainloop()