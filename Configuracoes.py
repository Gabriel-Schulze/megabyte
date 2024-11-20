from customtkinter import *
from tkinter import Frame


class Configuracoes:
    
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Configurações")
        self.root.geometry('600x400+300+80')

        CTkLabel(self.root,text="Configurações",font=("Open Sans bold",28)).pack(pady=(30,10))

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.frame4 = Frame(self.root)
        self.frame4.pack()
    
    
    
if __name__ == "__main__":
    root = CTk()
    app = Configuracoes(root)
    root.mainloop()