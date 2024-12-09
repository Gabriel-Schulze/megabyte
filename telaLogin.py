from customtkinter import *
from tkinter import Frame,ttk

class telaLogin:
    def __init__(self,root:CTk):
        self.root = root
        self.root.geometry("550x400")

        CTkLabel(self.root,text="LOGIN",font=("Open Sans bold",28)).pack(pady=(100,30))#grid(column=1,row=1, columnspan=2, pady=(0,30))
        

        self.frame1 = Frame(self.root)
        self.frame1.pack(anchor=W, padx=(50,0))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root)
        self.frame3.pack()
     
        self.createWidget()

    def createWidget(self):

        CTkLabel(self.frame1, text="Usuario:", font=("Open Sans",26), width=150).grid(column=1,row=1)
        CTkLabel(self.frame2, text="Senha:", font=("Open Sans",26), width=150).grid(column=1,row=1)
        
        self.usuario = CTkEntry(self.frame1,width=250)
        self.usuario.grid(column=2,row=1,)

        self.senha = CTkEntry(self.frame2,width=250)
        self.senha.grid(column=2,row=1,)

        self.btn_entrar = CTkButton(self.frame3, text="Entrar",width=10 ,command=self.entrar)
        self.btn_entrar.grid(column=2,row=1,sticky=E)
        
    
    def entrar(self):
        pass

if __name__ == "__main__":
    root = CTk()
    app = telaLogin(root)
    root.mainloop()