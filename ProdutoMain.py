from customtkinter import *
from tkinter import Frame,ttk
from PIL import Image
from EditarProduto import EditarProduto
from CadastroProduto import CadastroProduto
from crudProduto import read_produto,read_produtoByName,delete_produto

class ProdutoMain:
    
    def __init__(self,root:Frame):
        self.root = root
        self.root.config(width=1400,height=810)
        self.root.pack_propagate(False)
        self.fontLabel = ("Open Sans bold",16)
        
        self.createWidget()
        
    def createWidget(self):
        
        CTkLabel(self.root,text="PRODUTOS",text_color="#fff",bg_color="#0322a2",font=("Open Sans bold",28)).pack(pady=(30,10))
        
        
        self.frame1 = Frame(self.root,background="#0322a2")
        self.frame1.pack(anchor=W, padx=(50,0))
        self.frame2 = Frame(self.root,background="#0322a2")
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root,background="#0322a2")
        self.frame3.pack(side="bottom",anchor=W)
        
        self.buscar_entry = CTkEntry(self.frame1,width=350,placeholder_text="Buscar por nome")
        self.buscar_entry.grid(column=1,row=1)
        
        iconeBuscar = CTkImage(light_image=Image.open("icons/searchIcon.png"))
        self.btn_buscar = CTkButton(self.frame1,text_color="#000",fg_color="#fff",image=iconeBuscar,text="",width=16, command=self.buscarUsuario)
        self.btn_buscar.grid(column=2,row=1,pady=20,padx=5)
        
        iconeRecarregar = CTkImage(light_image=Image.open("icons/refreshIcon.png"))
        self.btn_attTabela = CTkButton(self.frame1,text_color="#000",fg_color="#fff",image=iconeRecarregar,text="",width=16,command=self.createLinhaTabela) 
        self.btn_attTabela.grid(column=3,row=1)

        ttk.Label(self.frame2,text="Código",width=8,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=1,row=1)
        ttk.Label(self.frame2,text="Descrição",width=45,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=2,row=1)
        ttk.Label(self.frame2,text="Valor",width=8,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=3,row=1)
        ttk.Label(self.frame2,text="Categoria",width=15,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=4,row=1)
        ttk.Label(self.frame2,text="Subcategoria",width=15,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=5,row=1)
        ttk.Label(self.frame2,text="",width=12,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=6,row=1)
        
        self.createLinhaTabela()

        self.btn_cadastrar = CTkButton(self.frame3,text_color="#000",fg_color="#fff", text="Cadastrar",width=120 ,command=self.telaCadastro,font=("Open Sans bold",16))
        self.btn_cadastrar.grid(column=2,row=1, padx=50,pady=100)
      
    def createLinhaTabela(self,buscar = ""):
        if buscar:
            data:list = read_produtoByName(buscar)
        else:
            data:list = read_produto()
        row=2
        
        for user in data:
            ttk.Label(self.frame2,text=user[0],width=8,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=1,row=row)
            ttk.Label(self.frame2,text=user[1],width=45,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=2,row=row)
            ttk.Label(self.frame2,text=user[2],width=8,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=3,row=row)
            ttk.Label(self.frame2,text=user[3],width=15,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=4,row=row)
            ttk.Label(self.frame2,text=user[4],width=15,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=5,row=row)
            editar = ttk.Label(self.frame2,text="Editar",width=6,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
            editar.grid(column=6,row=row,sticky=W)
            deletar = ttk.Label(self.frame2,text="Deletar",width=6,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
            deletar.grid(column=6,row=row,sticky=E)

            editar.bind("<Button-1>", lambda e,user=user[0]: self.telaEditar(user))
            deletar.bind("<Button-1>",lambda e,user=user[0]: self.deletarUsuario(user))
            
            row += 1
    
    def deletarUsuario(self,id):
        delete_produto(id)
        for widgets in self.frame2.winfo_children():
            gridInfo = widgets.grid_info()
            if gridInfo["row"] >= 2:
                widgets.destroy()
        self.createLinhaTabela()
    
    def buscarUsuario(self):
        nome = self.buscar_entry.get()
        
        if nome:
            for widgets in self.frame2.winfo_children():
                gridInfo = widgets.grid_info()
                if gridInfo["row"] >= 2:
                    widgets.destroy()
            self.createLinhaTabela(buscar=nome)
            
        self.buscar_entry.delete(0, END)

    def telaEditar(self,id):
        topEditar = CTkToplevel()
        topEditar.transient(self.root)
        topEditar.focus_force()
        EditarProduto(topEditar,id)
        
    def telaCadastro(self):
        topCadastro = CTkToplevel()
        topCadastro.transient(self.root)
        topCadastro.focus_force()
        CadastroProduto(topCadastro,1) # ID DO USUARIO
            
        
        
    
if __name__ == "__main__":
    root = CTk()
    app = ProdutoMain(root)
    root.mainloop()