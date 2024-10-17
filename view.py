# view.py

from tkinter import ttk, Label, Frame
import tkinter
from PIL import Image, ImageTk
from model import Ladrillo


class Vista:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Ladrillos")
        self.master.geometry("800x800+600+100")
        self.master.resizable(False,False)

        # Cargar y configurar la imagen de fondo
        self.fondo_imagen = Image.open('paredDeLadrillos.jpeg')
        self.fondo_imagen = self.fondo_imagen.resize((800, 800), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.fondo_imagen)

        # Colocar la imagen de fondo en un Label
        self.fondo_label = Label(self.master, image=self.fondo)
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Hacer que ocupe toda la ventana

        # Crear un frame central para agrupar los widgets
        self.frame_central = Frame(master, bg="tan1")
        self.frame_central.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el frame en la ventana

        self.tipo_ladrillo_var = tkinter.StringVar()

        self.fuente = ("Times New Roman", 16)

        # Crear estilo personalizado para los botones
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 14))  # Definir fuente de los botones

        # Widgets dentro del frame central
        self.label_tipo_ladrillo = ttk.Label(self.frame_central, text="Tipos de ladrillos:", font=self.fuente)
        self.tipo_ladrillo_menu = ttk.Combobox(self.frame_central, textvariable=self.tipo_ladrillo_var, 
                                               values=list(Ladrillo.tipos_ladrillos.keys()), font=self.fuente)
        self.tipo_ladrillo_menu.set(list(Ladrillo.tipos_ladrillos.keys())[0])  # Establecer el valor predeterminado

        self.label_altura_pared = ttk.Label(self.frame_central, text="Altura de la pared (m):", font=self.fuente)
        self.entry_altura_pared = ttk.Entry(self.frame_central, font=self.fuente)

        self.label_largo_pared = ttk.Label(self.frame_central, text="Largo de la pared (m):", font=self.fuente)
        self.entry_largo_pared = ttk.Entry(self.frame_central, font=self.fuente)

        # Botones con estilo personalizado
        self.calcular_button = ttk.Button(self.frame_central, text="Calcular", style="TButton")
        self.reset_button = ttk.Button(self.frame_central, text="Resetear", style="TButton")
        
        self.resultado_label = ttk.Label(self.frame_central, text="Resultado: ", font=self.fuente)
        self.resultado_cal = ttk.Label(self.frame_central, text="Cantidad de Cal: ", font=self.fuente)
        self.resultado_cemento = ttk.Label(self.frame_central, text="Cantidad de Cemento: ", font=self.fuente)
        self.resultado_arena = ttk.Label(self.frame_central, text="Cantidad de Arena:", font=self.fuente)

        # Ubicar los widgets dentro del frame central usando grid
        self.label_tipo_ladrillo.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.tipo_ladrillo_menu.grid(row=0, column=1, padx=10, pady=10)

        self.label_altura_pared.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_altura_pared.grid(row=1, column=1, padx=10, pady=10)

        self.label_largo_pared.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_largo_pared.grid(row=2, column=1, padx=10, pady=10)

        # Colocar los botones en la misma fila, uno al lado del otro
        self.calcular_button.grid(row=3, column=0, padx=(10, 5), pady=20, sticky="e")  # Botón "Calcular"
        self.reset_button.grid(row=3, column=1, padx=(5, 10), pady=20, sticky="w")  # Botón "Resetear"

        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=10)
        self.resultado_cal.grid(row=5, column=0, columnspan=2, pady=10)
        self.resultado_cemento.grid(row=6, column=0, columnspan=2, pady=10)
        self.resultado_arena.grid(row=7, column=0, columnspan=2, pady=10)

        self.master.resizable(False, False)


    def set_calcular_command(self, command):
        self.calcular_button.config(command=command)

    def mostrar_resultados(self, cantidad_ladrillos, cantidad_cal, cantidad_cemento, cantidad_arena):
        self.resultado_label.config(text=f"Cantidad de {self.tipo_ladrillo_var.get()}s necesarios: {cantidad_ladrillos}")
        self.resultado_cal.config(text=f"Cantidad de cal necesaria: {cantidad_cal} kg")
        self.resultado_cemento.config(text=f"Cantidad de cemento necesario: {cantidad_cemento} kg")
        self.resultado_arena.config(text=f"Cantidad de arena necesaria: {cantidad_arena} metros cúbicos")
    
    # Limpiar campos
    def set_reset_comand(self, command):
        self.reset_button.config(command=command)

    def limpiar_campos(self):
        self.entry_altura_pared.delete(0,'end')
        self.entry_largo_pared.delete(0,'end')
        self.resultado_cal.config(text='cantidad de Cal: ')
        self.resultado_cemento.config(text='cantidad de Cemento: ')
        self.resultado_arena.config(text='cantidad de Arena: ')
        self.resultado_label.config(text='Resultado: ')
