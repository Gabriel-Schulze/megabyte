from customtkinter import *
from tkinter import Frame,ttk,messagebox
from PIL import Image
from crudSubcategoria import delete_subcategoria,read_subcategoriaByCategoria
from CadastroCategoria import CadastroCategoria
from EditarCategoria import EditarCategoria
import mysql.connector.errors

class CategoriaMain:
    
    def __init__(self,root:Frame):
        self.root = root
        self.root.config(width=1400,height=810)
        self.root.pack_propagate(False)
        self.fontLabel = ("Open Sans bold",18)
        
        self.createWidget()
        
    def createWidget(self):
        
        CTkLabel(self.root,text_color="#fff",bg_color="#0322a2",text="SUBCATEGORIAS",font=("Open Sans bold",28)).pack(pady=(30,10))
        
        self.frame1 = Frame(self.root,background="#0322a2")
        self.frame1.pack(anchor=SE, padx=330,pady=(100,5))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=CENTER, padx=(50,0))
        self.frame3 = Frame(self.root,background="#0322a2")
        self.frame3.pack(side="bottom",anchor=W)
        
        logoRefresh = CTkImage(light_image=Image.open("icons/refreshIcon.png"))
        self.btn_refresh = CTkButton(self.frame1,fg_color="#fff",text="",image=logoRefresh,width=10,command=lambda: self.createLinhaTabela(1))
        self.btn_refresh.grid(column=1,row=1)
        
        self.frameLeft = Frame(self.frame2)
        self.frameLeft.grid(column=1,row=1,sticky=N)
        self.frameRight = Frame(self.frame2)
        self.frameRight.grid(column=2,row=1,sticky=N)
        
        self.hardwareLabel = ttk.Label(self.frameLeft,text="Hardwares",width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
        self.hardwareLabel.grid(column=1,row=1)
        self.hardwareLabel.bind("<Button-1>", lambda e: self.createLinhaTabela(categoria=1))
        
        self.perifericoLabel = ttk.Label(self.frameLeft,text="Periféricos",width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
        self.perifericoLabel.grid(column=1,row=2)
        self.perifericoLabel.bind("<Button-1>", lambda e: self.createLinhaTabela(categoria=2))
        
        self.monitoresLabel = ttk.Label(self.frameLeft,text="Monitores",width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
        self.monitoresLabel.grid(column=1,row=3)
        self.monitoresLabel.bind("<Button-1>", lambda e: self.createLinhaTabela(categoria=3))
        
        self.cadeiraLabel = ttk.Label(self.frameLeft,text="Cadeiras Gamers",width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
        self.cadeiraLabel.grid(column=1,row=4)
        self.cadeiraLabel.bind("<Button-1>", lambda e: self.createLinhaTabela(categoria=4))
        
        self.notebookLabel = ttk.Label(self.frameLeft,text="Notebooks",width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
        self.notebookLabel.grid(column=1,row=5)
        self.notebookLabel.bind("<Button-1>", lambda e: self.createLinhaTabela(categoria=5))
        
        self.createLinhaTabela(categoria=1)

        self.btn_cadastrar = CTkButton(self.frame3,text_color="#000",fg_color="#fff", text="Cadastrar",width=120 ,command=self.telaCadastro,font=("Open Sans bold",16))
        self.btn_cadastrar.grid(column=2,row=1, padx=50,pady=100)
      
    def createLinhaTabela(self,categoria):
        
        self.highlightCategoria(categoria)
        
        for widget in self.frameRight.winfo_children():
            widget.destroy()
        
        data = read_subcategoriaByCategoria(categoria)
        row = 1
        for subcateg in data:
            ttk.Label(self.frameRight,text=subcateg[1],width=20,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER).grid(column=1,row=row)
            
            editar = ttk.Label(self.frameRight,text="Editar",width=6,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
            editar.grid(column=2,row=row,sticky=W)
            deletar = ttk.Label(self.frameRight,text="Deletar",width=6,font=self.fontLabel,borderwidth=2,relief="solid",anchor=CENTER)
            deletar.grid(column=3,row=row,sticky=E)

            editar.bind("<Button-1>", lambda e,id=subcateg[0]: self.telaEditar(id))
            deletar.bind("<Button-1>",lambda e,id=subcateg[0]: self.deletarUsuario(id))
            
            row += 1
    
    def deletarUsuario(self,id):
        try:
            delete_subcategoria(id)
            for widgets in self.frame2.winfo_children():
                gridInfo = widgets.grid_info()
                if gridInfo["row"] >= 2:
                    widgets.destroy()
            self.createLinhaTabela(categoria=1)
        except mysql.connector.Error:
            messagebox.showerror("Impossível deletar","Impossível deletar pois há produtos vinculados a está subcategoria")
    def highlightCategoria(self,categoria):

        if categoria == 1:
            self.hardwareLabel.config(background="lightgray")
            self.perifericoLabel.config(background="white")
            self.monitoresLabel.config(background="white")
            self.cadeiraLabel.config(background="white")
            self.notebookLabel.config(background="white")
        elif categoria == 2:
            self.hardwareLabel.config(background="white")
            self.perifericoLabel.config(background="lightgray")
            self.monitoresLabel.config(background="white")
            self.cadeiraLabel.config(background="white")
            self.notebookLabel.config(background="white")
        elif categoria == 3:
            self.hardwareLabel.config(background="white")
            self.perifericoLabel.config(background="white")
            self.monitoresLabel.config(background="lightgray")
            self.cadeiraLabel.config(background="white")
            self.notebookLabel.config(background="white")
        elif categoria == 4:
            self.hardwareLabel.config(background="white")
            self.perifericoLabel.config(background="white")
            self.monitoresLabel.config(background="white")
            self.cadeiraLabel.config(background="lightgray")
            self.notebookLabel.config(background="white")
        elif categoria == 5:
            self.hardwareLabel.config(background="white")
            self.perifericoLabel.config(background="white")
            self.monitoresLabel.config(background="white")
            self.cadeiraLabel.config(background="white")
            self.notebookLabel.config(background="lightgray")
        
            
    def telaEditar(self,id):
        topEditar = CTkToplevel()
        topEditar.transient(self.root)
        topEditar.focus_force()
        EditarCategoria(topEditar,id)
        
    def telaCadastro(self):
        topCadastro = CTkToplevel()
        topCadastro.transient(self.root)
        topCadastro.focus_force()
        CadastroCategoria(topCadastro)
            
        
        
    
if __name__ == "__main__":
    root = CTk()
    app = CategoriaMain(root)
    root.mainloop()