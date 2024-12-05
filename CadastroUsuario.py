from customtkinter import *
from tkinter import Frame,messagebox
import re
from crudUsuario import create_usuario

class CadastroUsuario:
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Cadastro de Usuario")
        self.root.geometry('600x400+300+80')
        self.fontLabel = ("Open Sans",26)
        self.fontEntry = ("Open Sans",16)

        CTkLabel(self.root,text="Cadastro de Usuario",font=("Open Sans bold",28)).pack(pady=(30,10))

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

        CTkLabel(self.frame1, text="Nome:", font=self.fontLabel,anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame2, text="CPF:", font=self.fontLabel,anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame2, text="Perfil:", font=self.fontLabel,anchor=W).grid(column=3,row=1)
        CTkLabel(self.frame3, text="Telefone:", font=self.fontLabel,anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame4, text="Email:", font=self.fontLabel,anchor=E, width=100).grid(column=1,row=1)
        CTkLabel(self.frame5, text="Senha:", font=self.fontLabel,anchor=E, width=100).grid(column=1,row=1)

        self.perfil_combobox = CTkComboBox(self.frame2, values=("Admin","Padrao"),width=85)
        self.perfil_combobox.grid(column=4,row=1)

        self.nome_entry = CTkEntry(self.frame1,font=self.fontEntry,width=300)
        self.nome_entry.grid(column=2,row=1)
    
        self.cpf_entry = CTkEntry(self.frame2,font=self.fontEntry,width=150)
        self.cpf_entry.grid(column=2,row=1, sticky=W)

        self.telefone_entry = CTkEntry(self.frame3,font=self.fontEntry,width=300)
        self.telefone_entry.grid(column=2,row=1)

        self.email_entry = CTkEntry(self.frame4,font=self.fontEntry,width=300)
        self.email_entry.grid(column=2,row=1)

        self.senha_entry = CTkEntry(self.frame5,font=self.fontEntry,width=300, show="*")
        self.senha_entry.grid(column=2,row=1)

        self.btn_voltar = CTkButton(self.frame6, text="Voltar ao menu", width=10,command=self.voltarAoMenu, )
        self.btn_voltar.grid(column=1,row=1, pady=10,sticky=W)

        self.btn_cadastrar = CTkButton(self.frame6, text="Cadastrar",width=10 ,command=self.cadastrarUsuario)
        self.btn_cadastrar.grid(column=2,row=1,sticky=E)

    def voltarAoMenu(self):
        self.root.destroy()

    def cadastrarUsuario(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        perfil = self.perfil_combobox.get().lower()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if nome and cpf and perfil and telefone and email and senha:
            if len(cpf) >= 11 and len(cpf) <= 14:
                cpf = cpf.replace(" ","")
                cpf = cpf.replace("-","")
                cpf = cpf.replace(".","")
                cpf = re.sub("(\d{3})(\d{3})(\d{3})(\d{2})",r"\1.\2.\3-\4",cpf)
                if len(telefone) >= 11 and len(telefone) <= 15:
                    telefone = telefone.replace(" ","")
                    telefone = telefone.replace("-","")
                    telefone = telefone.replace("(","")
                    telefone = telefone.replace(")","")
                    telefone = re.sub("(\d{2})(\d{5})(\d{4})",r"(\1)\2-\3",telefone)

                    if re.match("(\w*)@(\w*)",email):
                        create_usuario(nome,cpf,telefone,perfil,email,senha)
                        messagebox.showinfo("SUCESSO!!","Cadastrado com sucesso!!")
                        self.root.destroy()
                    else:
                        messagebox.showinfo("Email inválido","Email inválido, confira antes de prosseguir")
                else:
                    messagebox.showinfo("Telefone inválido","O telefone deve ter no mínimo 11 caracteres e no máximo 16")
            else:
                messagebox.showinfo("CPF invalido","CPF deve ter no minimo 11 caracteres e no maximo 14")    
        else:
            messagebox.showinfo("Atenção!!","Preencha todos os campos!!")

if __name__ == "__main__":
    root = CTk()
    app = CadastroUsuario(root)
    root.mainloop()