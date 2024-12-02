import pandas as pd
from pandastable import Table,TableModel
from tkinter import *
from crudFornecedor import *


class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, user,parent):
        self.parent = parent
        self.user = user
        self.parent.geometry('800x600+200+100')
        self.parent.title('Table app')
        f = Frame(self.parent)
        f.pack(fill=BOTH,expand=1)

        
        data = read_fornecedor()
        
        df = pd.DataFrame({
            "Nome": [x[1] for x in data],
            "CNPJ": [x[2] for x in data],
            "Endereco":[x[3] for x in data],
            "Telefone": [x[4] for x in data]
        })
        
        self.table = pt = Table(f, dataframe=df,editable=False)
        pt.show()
        
        
        Label(f,text=user).grid(column=1,row=1)


if __name__ == "__main__":
    root = Tk()
    app = TestApp("TESTE",root)
    root.mainloop()

