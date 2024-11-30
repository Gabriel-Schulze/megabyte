from customtkinter import *
from tkinter import Frame

class Inicio:
    
    def __init__(self,root: CTk):
        self.root = root
        #self.root.geometry("1400x800")
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        self.frame1 = Frame(self.root,background="darkblue")
        self.frame1.grid(column=2,row=2,columnspan=2)
        
        CTkLabel(self.frame1, text="Inicio").grid(column=2,row=1, columnspan=2)
        
        
        CTkLabel(self.frame1,text="PLACEHOLDER",width=1370,height=380,bg_color="grey").grid(column=1,row=1,columnspan=2,pady=10)
        
        self.frame2 = Frame(self.frame1,background="darkblue")
        self.frame2.grid(column=2,row=3)
        
        CTkLabel(self.frame2, text="PLACEHOLDER", width=680, bg_color="grey",height=380).grid(column=1,row=1,padx=(10,5),pady=10)
        
        CTkLabel(self.frame2, text="PLACEHOLDER", width=680, bg_color="grey",height=380).grid(column=2,row=1,padx=(5,10),pady=10)
        
        

if __name__ == "__main__":
    root = CTk()
    app = Inicio(root)
    root.mainloop()