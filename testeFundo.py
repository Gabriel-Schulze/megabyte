from tkinter import Canvas, Frame
from customtkinter import *
from PIL import Image, ImageTk
import os

class telaLogin:
    def __init__(self, root: CTk):
        self.root = root
        self.root.geometry("550x400")

        # Caminho da imagem de fundo
        img_path = r"C:\Users\cibele_Karl\Downloads\projeto\megabyte\bg.png"

        if os.path.exists(img_path):
            # Carrega e redimensiona a imagem de fundo
            self.bg_image = Image.open(img_path)
            self.bg_image = self.bg_image.resize((550, 400))  # Ajusta a imagem ao tamanho da tela
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
            # Criando o Canvas para a imagem de fundo
            self.canvas = Canvas(self.root, width=550, height=400)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Frame para o nome de usuário e senha
        self.frame1 = Frame(self.root)  
        self.frame1.place(relx=0.5, rely=0.4, anchor='center')  # Posiciona na tela

        self.frame2 = Frame(self.root)  
        self.frame2.place(relx=0.5, rely=0.5, anchor='center')  # Posiciona na tela

        self.frame3 = Frame(self.root)  
        self.frame3.place(relx=0.5, rely=0.6, anchor='center')  # Posiciona na tela

        # Criando os widgets dentro dos frames
        self.createWidget()

    def createWidget(self):
        # Rótulo e campo de entrada para o nome de usuário
        CTkLabel(self.frame1, text="Usuario:", font=("Open Sans", 26), width=150, fg_color="white").grid(column=1, row=1)
        self.usuario = CTkEntry(self.frame1, width=250)
        self.usuario.grid(column=2, row=1)

        # Rótulo e campo de entrada para a senha
        CTkLabel(self.frame2, text="Senha:", font=("Open Sans", 26), width=150, fg_color="white").grid(column=1, row=1)
        self.senha = CTkEntry(self.frame2, width=250)
        self.senha.grid(column=2, row=1)

        # Botão "Entrar"
        self.btn_entrar = CTkButton(self.frame3, text="Entrar", width=10, command=self.entrar)
        self.btn_entrar.grid(column=2, row=1, sticky=E)

    def entrar(self):
        pass

if __name__ == "__main__":
    print("Iniciando a interface gráfica...")
    root = CTk()
    app = telaLogin(root)
    root.mainloop()

