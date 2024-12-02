from customtkinter import *
from tkinter import Frame
from PIL import Image
from Inicio import Inicio
from CadastroCategoria import CadastroCategoria
from CadastroProduto import CadastroProduto
from CadastroUsuario import CadastroUsuario

class Main:
    
    def __init__(self,user,root: CTk):
        self.user = user
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Pagina principal")
        self.root.geometry('1600x900+180+80')
        
        self.fontMenu = ("Open Sans",22)
    
        self.frame1 = Frame(self.root,background="red")
        self.frame1.pack()
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        self.frame2 = Frame(self.frame1,background="green")
        self.frame2.grid(column=1,row=1,rowspan=2,sticky=N)
        
        self.frameAdm = Frame(self.frame2,background="white")
        self.frameAdm.grid(column=1,row=0)
        
        logo = CTkImage(light_image=Image.open("admIcon.png"))
        
        CTkLabel(self.frameAdm, image=logo,text="").grid(column=1,row=0)
        CTkLabel(self.frameAdm, text="Administrador",font=("Open Sans",19)).grid(column=2,row=0)
        
        
        self.inicioLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Inicio")
        self.inicioLink.grid(column=1,row=1, columnspan=2,pady=(150,20))
        self.usuarioLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Usuario")
        self.usuarioLink.grid(column=1,row=2, columnspan=2,pady=(10,20))
        self.produtoLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Produtos")
        self.produtoLink.grid(column=1,row=3, columnspan=2,pady=(10,20))
        self.categLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Categorias")
        self.categLink.grid(column=1,row=4, columnspan=2,pady=(10,20))
        self.fornLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Fornecedores")
        self.fornLink.grid(column=1,row=5, columnspan=2,pady=(10,276))
        self.configLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Configurações")
        self.configLink.grid(column=1,row=6, columnspan=2,pady=(10,20))
        
        CTkLabel(self.frame2,text="Version 1.0").grid(column=1,row=7)
        CTkLabel(self.frame2 ,text="Logoff").grid(column=2,row=7)
        
        
        
        
        self.frame3 = Frame(self.frame1,background="red")
        self.frame3.grid(column=2,row=1,rowspan=2)
        
        #Inicio(self.frame3)
        
        
    
    def abrirCadastroCategoria(self):
        CadastroCategoria(self.frame2)
        
    def abrirCadastroProduto(self):
        self.top = CTkToplevel()
        CadastroProduto(self.top)
        
    def abrirCadastroUsuario(self):
        self.top = CTkToplevel()
        CadastroUsuario(self.top)
        
if __name__ == "__main__":
    root = CTk()
    app = Main("admin",root)
    root.mainloop()