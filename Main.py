from customtkinter import *
from tkinter import Frame
from PIL import Image
from Inicio import Inicio
from UsuarioMain import UsuarioMain
from ProdutoMain import ProdutoMain
from CategoriaMain import CategoriaMain
from FornecedorMain import FornecedorMain
import sys
import subprocess

class Main:
    
    def __init__(self,user,root: CTk):
        self.user = user
        self.root = root
        root.protocol("WM_DELETE_WINDOW", self.on_closing) 
        self.root.resizable(False, False)
        self.root.title("Pagina principal")
        self.root.geometry('1600x810+180+80')
        self.root.config(background="darkblue")
        
        self.fontMenu = ("Open Sans",22)
    
        self.frame1 = Frame(self.root,background="darkblue")
        self.frame1.pack()
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        self.frame2 = Frame(self.frame1,background="green")
        self.frame2.grid(column=1,row=1,rowspan=2)
        self.frame2.config(width=210,height=810)
        self.frame2.pack_propagate(False)
        
        
        self.frameAdm = Frame(self.frame2,background="green")
        self.frameAdm.grid(column=1,row=0,columnspan=2,pady=(10,0))
        
        logoAdm = CTkImage(light_image=Image.open("icons/admIcon.png"))
        
        CTkLabel(self.frameAdm, image=logoAdm,text="").grid(column=1,row=0,padx=(0,5))
        
        CTkLabel(self.frameAdm, text=sys.argv[2],font=("Open Sans",19)).grid(column=2,row=0)
            
        
        self.inicioLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Inicio")
        self.inicioLink.grid(column=1,row=1, columnspan=2,pady=(150,20))
        self.inicioLink.bind("<Button-1>", lambda e: self.telaInicio())
        
        if self.user == "admin":
            self.usuarioLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Usuario")
            self.usuarioLink.grid(column=1,row=2, columnspan=2,pady=(10,20))
            self.usuarioLink.bind("<Button-1>", lambda e: self.telaUsuario())
        
        self.produtoLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Produtos")
        self.produtoLink.grid(column=1,row=3, columnspan=2,pady=(10,20))
        self.produtoLink.bind("<Button-1>", lambda e: self.telaProduto())
        
        self.categLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Categorias")
        self.categLink.grid(column=1,row=4, columnspan=2,pady=(10,20))
        self.categLink.bind("<Button-1>", lambda e: self.telaCategoria())
        
        self.fornLink = CTkLabel(self.frame2,font=self.fontMenu ,text="Fornecedores",width=210)
        self.fornLink.grid(column=1,row=5, columnspan=2,pady=(10,280))
        self.fornLink.bind("<Button-1>", lambda e: self.telaFornecedor())

        if self.user != "admin":
            self.fornLink.grid(column=1,row=5, columnspan=2,pady=(10,340))
        
        self.frameConfig = Frame(self.frame2,background="green")
        self.frameConfig.grid(column=1,row=6,columnspan=2)
        
        logoConfig = CTkImage(light_image=Image.open("icons/configureIcon.png"))
        
        CTkLabel(self.frameConfig, image=logoConfig,text="").grid(column=1,row=1,padx=(0,5))
        self.configLink = CTkLabel(self.frameConfig,font=self.fontMenu ,text="Configurações")
        self.configLink.grid(column=2,row=1)
        
        CTkLabel(self.frame2,text="Version 1.0",anchor=S).grid(column=1,row=7,sticky=W,padx=5)
        self.btn_Logoof = CTkLabel(self.frame2 ,text="LogOff",font=("Open Sans",18),text_color="darkred")
        self.btn_Logoof.grid(column=2,row=7,pady=(10,0))
        self.btn_Logoof.bind("<Button-1>", lambda e: self.logOff() )
        
        self.frame3 = Frame(self.frame1,background="#0322a2")
        self.frame3.grid(column=2,row=1,rowspan=2)
        
        self.inicio = Inicio(self.frame3)
        
    def logOff(self):
        subprocess.Popen([sys.executable,"telaLogin.py"])
        sys.exit()
     
    def telaInicio(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        Inicio(self.frame3)  
       
    def telaUsuario(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        UsuarioMain(self.frame3)  
        
    def telaProduto(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        ProdutoMain(self.frame3) 
        
    def telaCategoria(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        CategoriaMain(self.frame3) 
    
    def telaFornecedor(self):
        for widgets in self.frame3.winfo_children():
            widgets.destroy()
        FornecedorMain(self.frame3) 
    
    def on_closing(self, event=0):
        subprocess.Popen([sys.executable,"telaLogin.py"]) 
        sys.exit()  
    
    
if __name__ == "__main__":
    root = CTk()
    app = Main(sys.argv[1],root)
    root.mainloop()