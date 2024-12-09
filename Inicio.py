from customtkinter import *
from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from crudProduto import read_produtoByLowStock

class Inicio:
    
    def __init__(self,root: CTk):
        self.root = root
        #root.protocol("WM_DELETE_WINDOW", self.on_closing) 
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        self.frame1 = Frame(self.root,background="#0322a2")
        self.frame1.grid(column=2,row=2,columnspan=2)
        self.frame1.config(width=1400,height=810)
        self.frame1.pack_propagate(False)
        
        #CTkLabel(self.frame1, text="Inicio").grid(column=2,row=1, columnspan=2)
        
        self.frameEstoque = Frame(self.frame1,width=1370,height=380)
        self.frameEstoque.grid(column=1,row=1,columnspan=2,pady=10)
        self.frameEstoque.pack_propagate(False)
        CTkLabel(self.frameEstoque,text="ESTOQUE EM NÍVEL CRÍTICO:",font=("Open Sans",24),text_color="red",height=10).grid(column=1,row=1)
        self.estoqueTextBox = CTkTextbox(self.frameEstoque,width=1370,height=370,font=("Open Sans",22), text_color="red",fg_color="#EEEEEE")
        self.estoqueTextBox.tag_config("center", justify='center')
        self.estoqueTextBox.grid(column=1,row=2)
        
        
        self.carregaEstoque()
        
        
        self.frame2 = Frame(self.frame1,background="#0322a2")
        self.frame2.grid(column=2,row=3)
        
        self.criar_grafico_pizza()

        self.criar_grafico_colunas()
        
    def carregaEstoque(self):
        estoque = read_produtoByLowStock()
        
        for produto in estoque:
            self.estoqueTextBox.insert(END,f"Produto: {produto[1]}, {produto[0]} peças  \n")
            self.estoqueTextBox.tag_add("center", "1.0", "end")
            
        self.estoqueTextBox.configure(state="disabled")
        
    def criar_grafico_pizza(self):
        categorias = ['Mouse', 'Teclado', 'Monitor', 'Placa de Video']
        valores = [25, 35, 20, 20]
        
        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(6.8, 3.8))
        ax.pie(valores, labels=categorias, autopct='%1.1f%%')
        ax.set_title('Fluxo de Saída no mês de Setembro')

        # Adição do gráfico ao frame usando FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1,row=1,padx=(10,5),pady=10)

    def criar_grafico_colunas(self):
        categorias = ['Mouse', 'Teclado', 'Monitor', 'Placa de Video']
        valores = [25, 35, 20, 20]
        
        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(6.8, 3.8))
        ax.bar(categorias,valores,color=['blue', 'green', 'red', 'purple'])
        ax.set_title('Quantidade Estoque x Saídas dos itens')

        # Adição do gráfico ao frame usando FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.draw()
        canvas.get_tk_widget().grid(column=2,row=1,padx=(5,10),pady=10)   
        
    def on_closing(self, event=0): 
        sys.exit()       

if __name__ == "__main__":
    root = CTk()
    app = Inicio(root)
    root.mainloop()