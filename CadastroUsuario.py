from customtkinter import *
from tkinter import Frame

class CadastroUsuario:
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Cadastro de Usuario")
        self.root.geometry('600x400+300+80')

        CTkLabel(self.root,text="Cadastro de Usuario",font=("Open Sans bold",28)).pack(pady=(30,10))#grid(column=1,row=1, columnspan=2, pady=(0,30))

        self.frame1 = Frame(self.root)
        self.frame1.pack(anchor=W, padx=(120,0))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=W, padx=(120,0))
        self.frame3 = Frame(self.root)
        self.frame3.pack(anchor=W, padx=(115,0))
        self.frame4 = Frame(self.root)
        self.frame4.pack(anchor=W, padx=(120,0))
        self.frame5 = Frame(self.root)
        self.frame5.pack(anchor=W, padx=(120,0))
        self.frame6 = Frame(self.root)
        self.frame6.pack()
        
        self.createWidget()

    def createWidget(self):

        CTkLabel(self.frame1, text="Nome:", font=("Open Sans",26),anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame2, text="CPF:", font=("Open Sans",26),anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame2, text="Perfil:", font=("Open Sans",26),anchor=W).grid(column=3,row=1)
        CTkLabel(self.frame3, text="Telefone:", font=("Open Sans",26),anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame4, text="Email:", font=("Open Sans",26),anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame5, text="Senha:", font=("Open Sans",26),anchor=E, width=100).grid(column=1,row=1)

        self.perfil_combobox = CTkComboBox(self.frame2, values=("Admin","Padrao"),width=85)
        self.perfil_combobox.grid(column=4,row=1)

        self.nome_entry = CTkEntry(self.frame1,font=("Open Sans",16),width=300)
        self.nome_entry.grid(column=2,row=1)
    
        self.cpf_entry = CTkEntry(self.frame2,font=("Open Sans",16),width=150)
        self.cpf_entry.grid(column=2,row=1, sticky=W)

        self.telefone_entry = CTkEntry(self.frame3,font=("Open Sans",16),width=300)
        self.telefone_entry.grid(column=2,row=1)

        self.email_entry = CTkEntry(self.frame4,font=("Open Sans",16),width=300)
        self.email_entry.grid(column=2,row=1)

        self.senha_entry = CTkEntry(self.frame5,font=("Open Sans",16),width=300, show="*")
        self.senha_entry.grid(column=2,row=1)

        self.btn_voltar = CTkButton(self.frame6, text="Voltar ao menu", width=10,command=self.voltarAoMenu, )
        self.btn_voltar.grid(column=1,row=1, pady=10,sticky=W)

        self.btn_cadastrar = CTkButton(self.frame6, text="Cadastrar",width=10 ,command=self.cadastrarUsuario)
        self.btn_cadastrar.grid(column=2,row=1,sticky=E)

    def voltarAoMenu(self):
        pass

    def cadastrarUsuario(self):
        pass

if __name__ == "__main__":
    root = CTk()
    app = CadastroUsuario(root)
    root.mainloop()