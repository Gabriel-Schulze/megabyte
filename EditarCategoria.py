from customtkinter import *
from tkinter import Frame,ttk,messagebox
from crudCategoria import read_categoria
from crudSubcategoria import read_subcategoriaById,update_subcategoria

class EditarCategoria:
    def __init__(self,root:CTk,id):
        self.root = root
        self.root.title("Editar de Categoria")
        self.root.geometry('600x400+300+80')
        self.id = id

        CTkLabel(self.root,text="Editar de Categoria",font=("Open Sans bold",28)).pack(pady=(30,10))

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

        self.btn_editar = CTkButton(self.frame3, text="Editar",width=10 ,command=self.salvarNovosDados)
        self.btn_editar.grid(column=2,row=1,sticky=E)
        
        self.carregaDados()
        
    def carregaDados(self):
        data = read_subcategoriaById(self.id)
        self.categoria_combobox.set(self.data_categorias[data[2] - 1])
        self.subcategoria_entry.insert(0, data[1])
    
    
    def voltarAoMenu(self):
        self.root.destroy()

    def salvarNovosDados(self):
        categoria = self.categoria_combobox.get()
        subcategoria = self.subcategoria_entry.get()
        
        if categoria and subcategoria:
            update_subcategoria(self.id,subcategoria,self.data_categorias.index(categoria) + 1,1)
            messagebox.showinfo("Sucesso!!", "Editado com sucesso!")
            self.root.destroy()
        else:
            messagebox.showinfo("Atenção", "Preencha todos os campos")

if __name__ == "__main__":
    root = CTk()
    app = EditarCategoria(root,1)
    root.mainloop()