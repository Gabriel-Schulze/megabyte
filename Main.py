from customtkinter import *
from tkinter import Frame
from CadastroCategoria import CadastroCategoria
from CadastroProduto import CadastroProduto
from CadastroUsuario import CadastroUsuario

class Main:
    
    def __init__(self,root: CTk):
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Pagina principal")
        self.root.geometry('1600x900+180+80')
        
    
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        CTkLabel(self.frame1, text="Administrador").grid(column=1,row=1)
        CTkLabel(self.frame1, text="Inicio").grid(column=2,row=1, columnspan=2)
        
        self.frame2 = Frame(self.frame1)
        self.frame2.grid(column=1,row=2,rowspan=2)
        
        CTkLabel(self.frame2, text="Inicio").grid(column=1,row=1, columnspan=2)
        CTkLabel(self.frame2, text="Usuario").grid(column=1,row=2, columnspan=2)
        CTkLabel(self.frame2, text="Produtos").grid(column=1,row=3, columnspan=2)
        CTkLabel(self.frame2, text="Categorias").grid(column=1,row=4, columnspan=2)
        CTkLabel(self.frame2, text="Fornecedores").grid(column=1,row=5, columnspan=2)
        CTkLabel(self.frame2, text="Configurações").grid(column=1,row=6, columnspan=2)
        CTkLabel(self.frame2, text="Version 1.0").grid(column=1,row=7)
        CTkLabel(self.frame2, text="Logoff").grid(column=2,row=7)
        
        self.frame3 = Frame(self.frame1)
        self.frame3.grid(column=2,row=2,columnspan=2)
        
        CTkLabel(self.frame3,text="LOREM IPSUM",width=1400).grid(column=1,row=1,columnspan=2)
        
               

    
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
    app = Main(root)
    root.mainloop()