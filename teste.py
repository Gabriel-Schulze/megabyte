from tkinter import *
from testePandasTable import TestApp

class Teste:
    
    def __init__(self,root:Tk):
        self.root = root
        self.root.geometry("800x400")
        self.root.title("Teste")
        
        Label(self.root,text="Login").grid(column=1,row=1)
        Label(self.root,text="Senha").grid(column=1,row=2)
        
        self.entryL = Entry(self.root)
        self.entryL.grid(column=2,row=1)
        self.entryS = Entry(self.root)
        self.entryS.grid(column=2,row=2)
        
        self.button = Button(self.root,text="Logar",command=self.valida)
        self.button .grid(column=1,row=3)
        
    def valida(self):
        self.top = Toplevel()
        TestApp(self.entryS.get(),self.top)
if __name__ == "__main__":
    root = Tk()
    app = Teste(root)
    root.mainloop()
        
        
        