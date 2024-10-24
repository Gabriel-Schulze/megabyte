import pandas as pd
from pandastable import Table,TableModel
from tkinter import *
from crudFornecedor import *


class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x600+200+100')
        self.main.title('Table app')
        f = Frame(self.main)
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
        return


app = TestApp()
#launch the app
app.mainloop()

