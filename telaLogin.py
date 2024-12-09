from customtkinter import *
from tkinter import Frame,messagebox
from crudUsuario import verify_usuario
import sys
import subprocess


class telaLogin:
    def __init__(self,root:CTk):
        self.root = root
        self.root.geometry("550x400")
        self.root.config(background="#0322a2")

        CTkLabel(self.root,text="LOGIN",text_color="#ffffff",bg_color="#0322a2",font=("Open Sans bold",28)).pack(pady=(100,30))#grid(column=1,row=1, columnspan=2, pady=(0,30))
        

        self.frame1 = Frame(self.root,background="#0322a2")
        self.frame1.pack(anchor=W, padx=(50,0))
        self.frame2 = Frame(self.root,background="#0322a2")
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root,background="#0322a2")
        self.frame3.pack()
        
        self.createWidget()

    def createWidget(self):

        CTkLabel(self.frame1, text="Email:",text_color="#ffffff",bg_color="#0322a2", font=("Open Sans",26), width=150,anchor=E).grid(column=1,row=1)
        CTkLabel(self.frame2, text="Senha:",text_color="#ffffff",bg_color="#0322a2", font=("Open Sans",26), width=150,anchor=E).grid(column=1,row=1)
        
        self.emailEntry = CTkEntry(self.frame1,text_color="#000000",width=250)
        self.emailEntry.grid(column=2,row=1,)

        self.senhaEntry = CTkEntry(self.frame2,text_color="#000000",width=250,show="*")
        self.senhaEntry.grid(column=2,row=1,)

        self.btn_entrar = CTkButton(self.frame3,text_color="#000000",bg_color="#0322a2",fg_color="#ffffff", text="Entrar",width=10 ,command=self.entrar)
        self.btn_entrar.grid(column=1,row=1,pady=10)
        
    
    def entrar(self):
        email = self.emailEntry.get()
        senha = self.senhaEntry.get()
        userExiste = verify_usuario(email,senha)
        
        if userExiste:
            subprocess.Popen([sys.executable,"Main.py",userExiste[0],userExiste[1]])
            sys.exit()
        else:
            messagebox.showinfo("Login inválido!!","Verifique se as infomações então corretas, ou contate um administrador para novo cadastro")

if __name__ == "__main__":
    root = CTk()
    app = telaLogin(root)
    root.mainloop()