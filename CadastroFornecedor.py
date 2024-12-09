from customtkinter import *
from tkinter import Frame,messagebox
from crudFornecedor import create_fornecedor
import re

class CadastroFornecedor:
    def __init__(self,root:CTk,id):
        self.root = root
        self.root.title("Cadastro de Fornecedor")
        self.root.geometry('600x400+300+80')
        self.id = id

        CTkLabel(self.root,text="Cadastro de Fornecedor",font=("Open Sans bold",28)).pack(pady=(30,10))#grid(column=1,row=1, columnspan=2, pady=(0,30))

        self.frame1 = Frame(self.root)
        self.frame1.pack(anchor=W, padx=(27,0))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root)
        self.frame3.pack(anchor=W, padx=(50,0))
        self.frame4 = Frame(self.root)
        self.frame4.pack(anchor=W, padx=(50,0))
        self.frame5 = Frame(self.root)
        self.frame5.pack()
        
        self.createWidget()

    def createWidget(self):

        CTkLabel(self.frame1, text="Nome da Empresa:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        CTkLabel(self.frame2, text="CNPJ:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        CTkLabel(self.frame3, text="Endereço:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        CTkLabel(self.frame4, text="Telefone:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        
        self.empresa_entry = CTkEntry(self.frame1,font=("Open Sans",16),width=300)
        self.empresa_entry.grid(column=2,row=1)
        
        self.cnpj_entry = CTkEntry(self.frame2,font=("Open Sans",16),width=300)
        self.cnpj_entry.grid(column=2,row=1)
        
        self.endereco_entry = CTkEntry(self.frame3,font=("Open Sans",16),width=300)
        self.endereco_entry.grid(column=2,row=1)
        
        self.contato_entry = CTkEntry(self.frame4,font=("Open Sans",16),width=300)
        self.contato_entry.grid(column=2,row=1)
        
        self.btn_voltar = CTkButton(self.frame5, text="Voltar ao menu", width=10,command=self.voltarAoMenu, )
        self.btn_voltar.grid(column=1,row=1, pady=10,sticky=W)

        self.btn_cadastrar = CTkButton(self.frame5, text="Cadastrar",width=10 ,command=self.cadastrarProduto)
        self.btn_cadastrar.grid(column=2,row=1,sticky=E)
        

    def voltarAoMenu(self):
        self.root.destroy()

    def cadastrarProduto(self):
        empresa = self.empresa_entry.get()
        cnpj = self.cnpj_entry.get()
        endereco = self.endereco_entry.get()
        contato = self.contato_entry.get()
        
        if empresa and cnpj and endereco and contato:
            if len(cnpj) >= 12 and len(cnpj) <= 15:
                cnpj = cnpj.replace(" ","")
                cnpj = cnpj.replace("-","")
                cnpj = cnpj.replace(".","")
                cnpj = cnpj.replace("/","")
                cnpj = re.sub("(\d{3})(\d{3})(\d{4})(\d{2})",r"\1.\2/\3-\4",cnpj)
                if len(contato) >= 11 and len(contato) <= 15:
                    contato = contato.replace(" ","")
                    contato = contato.replace("-","")
                    contato = contato.replace("(","")
                    contato = contato.replace(")","")
                    contato = re.sub("(\d{2})(\d{5})(\d{4})",r"(\1)\2-\3",contato)
                    
                    create_fornecedor(empresa,cnpj,endereco,contato,self.id)
                    messagebox.showinfo("SUCESSO!!","Cadastrado com sucesso!!")
                    self.root.destroy()
                else:
                    messagebox.showinfo("Telefone inválido","O telefone deve ter no minimo 11 caracteres e no maximo 16")
            else:
                messagebox.showinfo("CNPJ invalido","CNPJ deve ter no minimo 12 caracteres e no maximo 15")
        else:
            messagebox.showinfo("Atenção", "Todos os campos dever ser preenchidos")

if __name__ == "__main__":
    root = CTk()
    app = CadastroFornecedor(root)
    root.mainloop()