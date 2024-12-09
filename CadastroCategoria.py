from customtkinter import *
from tkinter import Frame,ttk,messagebox
from crudSubcategoria import create_subcategoria

class CadastroCategoria:
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Cadastro de Categoria")
        self.root.geometry('600x400+600+80')

        CTkLabel(self.root,text="Cadastro de Categoria",font=("Open Sans bold",28)).pack(pady=(30,10))#grid(column=1,row=1, columnspan=2, pady=(0,30))

        self.frame1 = Frame(self.root)
        self.frame1.pack(anchor=W, padx=(50,0))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        
        self.data_categorias = ("HARDWARES","PERIFÉRICOS","MONITORES","CADEIRAS GAMERS","NOTEBOOKS")
        self.createWidget()

    def createWidget(self):

        CTkLabel(self.frame1, text="Categoria:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        CTkLabel(self.frame2, text="Subcategoria:", font=("Open Sans",26),anchor=E, width=200).grid(column=1,row=1)
        
        self.categoria_combobox = ttk.Combobox(self.frame1, values=[x for x in self.data_categorias],width=46, state="readonly")
        self.categoria_combobox.grid(column=2,row=1)
       
        
        self.subcategoria_entry = CTkEntry(self.frame2,width=300)
        self.subcategoria_entry.grid(column=2,row=1)
        
     
        self.btn_voltar = CTkButton(self.frame3, text="Voltar ao menu", width=10,command=self.voltarAoMenu, )
        self.btn_voltar.grid(column=1,row=1, pady=10,sticky=W)

        self.btn_cadastrar = CTkButton(self.frame3, text="Cadastrar",width=10 ,command=self.cadastrarProduto)
        self.btn_cadastrar.grid(column=2,row=1,sticky=E)
        
    def voltarAoMenu(self):
        self.root.destroy()

    def cadastrarProduto(self):
        categoria = self.categoria_combobox.get()
        subcategoria = self.subcategoria_entry.get()
        
        if categoria and subcategoria:
            create_subcategoria(subcategoria,self.data_categorias.index(categoria) + 1,1)
            messagebox.showinfo("Sucesso!!", "Cadastrado com sucesso!")
            self.root.destroy()
        else:
            messagebox.showinfo("Atenção", "Preencha todos os campos")

if __name__ == "__main__":
    root = CTk()
    app = CadastroCategoria(root)
    root.mainloop()