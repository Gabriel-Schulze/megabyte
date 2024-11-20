from customtkinter import *
from tkinter import Frame


class Configuracoes:
    
    def __init__(self,root:CTk):
        self.root = root
        self.root.title("Configurações")
        self.root.geometry('600x400+300+80')
    
    
    
    
if __name__ == "__main__":
    root = CTk()
    app = Configuracoes(root)
    root.mainloop()