import pandas as pd
from pandastable import Table,TableModel
from tkinter import *
from crudFornecedor import *
import re
class TestApp(Frame):
    def __init__(self,root):

        
        email = "adoasdako@sadkaskd"
        if re.match("(\w*)@(\w*)",email):
            pass
        else:
            print("invalido")
        #print(cpf)



if __name__ == "__main__":
    root = Tk()
    app = TestApp(root)
    root.mainloop()

