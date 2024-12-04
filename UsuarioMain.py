from customtkinter import *
from tkinter import Frame,ttk
from PIL import Image
from crudUsuario import read_usuario
from EditarUsuario import EditarUsuario
from CadastroUsuario import CadastroUsuario

class UsuarioMain:
    
    def __init__(self,user,root:Frame):
        self.root = root
        #self.root.geometry("1400x800")      
        
        self.createWidget()
        
    def createWidget(self):
        
        CTkLabel(self.root,text="USUÁRIOS",font=("Open Sans bold",28)).pack(pady=(30,10))#grid(column=1,row=1, columnspan=2, pady=(0,30))
        
        CTkLabel(self.root,text="",width=1390).pack()
        
        self.frame1 = Frame(self.root)
        self.frame1.pack(anchor=W, padx=(50,0))
        self.frame2 = Frame(self.root)
        self.frame2.pack(anchor=W, padx=(50,0))
        self.frame3 = Frame(self.root)
        self.frame3.pack(side="bottom",anchor=W)
        
        self.buscar_entry = CTkEntry(self.frame1,width=350,placeholder_text="Buscar")
        self.buscar_entry.grid(column=1,row=1)
        
        iconeBuscar = CTkImage(light_image=Image.open("iconeBuscar.png"))
        self.btn_buscar = CTkButton(self.frame1,image=iconeBuscar,text="",width=16)
        self.btn_buscar.grid(column=2,row=1,pady=20)
        
        self.btn_attTabela = CTkButton(self.frame1,text="Recarregar",width=16,command= self.createLinhaTabela) 
        self.btn_attTabela.grid(column=3,row=1)

        ttk.Label(self.frame2,text="Código",width=8,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=1,row=1)
        ttk.Label(self.frame2,text="Nome",width=25,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=2,row=1)
        ttk.Label(self.frame2,text="Telefone",width=15,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=3,row=1)
        ttk.Label(self.frame2,text="E-mail",width=25,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=4,row=1)
        ttk.Label(self.frame2,text="CPF",width=15,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=5,row=1)
        ttk.Label(self.frame2,text="",width=6,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=6,row=1)
        
        self.createLinhaTabela()

        self.btn_cadastrar = CTkButton(self.frame3, text="Cadastrar",width=120 ,command=self.telaCadastro,font=("Open Sans bold",16))
        self.btn_cadastrar.grid(column=2,row=1, padx=50,pady=100)
      
    def createLinhaTabela(self):
        data:list = read_usuario()
        row=2
        for user in data:
            ttk.Label(self.frame2,text=user[0],width=8,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=1,row=row)
            ttk.Label(self.frame2,text=user[1],width=25,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=2,row=row)
            ttk.Label(self.frame2,text=user[2],width=15,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=3,row=row)
            ttk.Label(self.frame2,text=user[3],width=25,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=4,row=row)
            ttk.Label(self.frame2,text=user[4],width=15,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER).grid(column=5,row=row)
            editar = ttk.Label(self.frame2,text="E",width=3,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER)
            editar.grid(column=6,row=row,sticky=W)
            deletar = ttk.Label(self.frame2,text="D",width=3,font=("Open Sans bold",16),borderwidth=2,relief="solid",anchor=CENTER)
            deletar.grid(column=6,row=row,sticky=E)

            editar.bind("<Button-1>", lambda e,user=user[0]: self.telaEditar(user))
            deletar.bind("<Button-1>",lambda e: self.telaEditar(user[0]))
            
            row += 1
            
    def telaEditar(self,id):
        topEditar = CTkToplevel()
        topEditar.transient(self.root)
        topEditar.focus_force()
        EditarUsuario(topEditar,id)
        
    def telaCadastro(self):
        topCadastro = CTkToplevel()
        topCadastro.transient(self.root)
        topCadastro.focus_force()
        CadastroUsuario(topCadastro)
            
        
        
    
if __name__ == "__main__":
    root = CTk()
    app = UsuarioMain("admin",root)
    root.mainloop()