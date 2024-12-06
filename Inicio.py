from customtkinter import *
from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Inicio:
    
    def __init__(self,root: CTk):
        self.root = root
        
        
        self.criandoWidgets()
        
    def criandoWidgets(self):
        
        self.frame1 = Frame(self.root,background="darkblue")
        self.frame1.grid(column=2,row=2,columnspan=2)
        self.frame1.config(width=1400,height=810)
        self.frame1.pack_propagate(False)
        
        CTkLabel(self.frame1, text="Inicio").grid(column=2,row=1, columnspan=2)
        
        
        CTkLabel(self.frame1,text="PLACEHOLDER",width=1370,height=380,bg_color="grey").grid(column=1,row=1,columnspan=2,pady=10)
        
        self.frame2 = Frame(self.frame1,background="darkblue")
        self.frame2.grid(column=2,row=3)
        
        self.criar_grafico_pizza()

        self.criar_grafico_colunas()
        
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

if __name__ == "__main__":
    root = CTk()
    app = Inicio(root)
    root.mainloop()