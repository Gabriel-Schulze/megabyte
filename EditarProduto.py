from customtkinter import *
from tkinter import Frame

class EditarFornecedor:
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Editar de Fornecedor")
        self.root.geometry('600x400+300+80')

        CTkLabel(self.root,text="Editar de Fornecedor",font=("Open Sans bold",28)).pack(pady=(30,10))#grid(column=1,row=1, columnspan=2, pady=(0,30))

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
        CTkLabel(self.frame4, text="Contato:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        
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

        self.btn_Editar = CTkButton(self.frame5, text="Editar",width=10 ,command=self.cadastrarProduto)
        self.btn_Editar.grid(column=2,row=1,sticky=E)
        

    def voltarAoMenu(self):
        pass

    def cadastrarProduto(self):
        pass

if __name__ == "__main__":
    root = CTk()
    app = EditarFornecedor(root)
    root.mainloop()