# view.py

from tkinter import ttk, Label
import tkinter
from PIL import Image, ImageTk
from model import Ladrillo


class Vista:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Ladrillos")
        self.master.geometry("600x600")
        self.master.configure(bg="SkyBlue3")
        
        # Cargar y configurar la imagen de fondo
        self.fondo_imagen = Image.open('paredDeLadrillos.jpeg')
        self.fondo_imagen = self.fondo_imagen.resize((600, 600), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.fondo_imagen)

        # Colocar la imagen de fondo en un Label
        self.fondo_label = Label(self.master, image=self.fondo)
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Hacer que ocupe toda la ventana

        # Crear y ubicar los widgets en la ventana (después de colocar la imagen de fondo)
        self.tipo_ladrillo_var = tkinter.StringVar()

        self.fuente = ("Arial", 12)
        self.label_tipo_ladrillo = ttk.Label(master, text="Tipos de ladrillos:", font=self.fuente)
        self.tipo_ladrillo_menu = ttk.Combobox(master, textvariable=self.tipo_ladrillo_var, 
                                               values=list(Ladrillo.tipos_ladrillos.keys()), font=self.fuente)
        self.tipo_ladrillo_menu.set(list(Ladrillo.tipos_ladrillos.keys())[0])  # Establecer el valor predeterminado

        self.label_altura_pared = ttk.Label(master, text="Altura de la pared (m):", font=self.fuente)
        self.entry_altura_pared = ttk.Entry(master, font=self.fuente)

        self.label_largo_pared = ttk.Label(master, text="Largo de la pared (m):", font=self.fuente)
        self.entry_largo_pared = ttk.Entry(master, font=self.fuente)

        self.calcular_button = ttk.Button(master, text="Calcular")

        self.resultado_label = ttk.Label(master, text="Resultado: ", font=self.fuente)
        self.resultado_cal = ttk.Label(master, text="Cantidad de Cal: ", font=self.fuente)
        self.resultado_cemento = ttk.Label(master, text="Cantidad de Cemento: ", font=self.fuente)
        self.resultado_arena = ttk.Label(master, text="Cantidad de Arena:", font=self.fuente)

        # Ubicar los widgets en la cuadrícula
        self.label_tipo_ladrillo.grid(row=1, column=1, padx=10, pady=30)
        self.tipo_ladrillo_menu.grid(row=1, column=2, padx=10, pady=10)

        self.label_altura_pared.grid(row=2, column=1, padx=10, pady=30)
        self.entry_altura_pared.grid(row=2, column=2, padx=10, pady=10)

        self.label_largo_pared.grid(row=3, column=1, padx=10, pady=30)
        self.entry_largo_pared.grid(row=3, column=2, padx=10, pady=10)

        self.calcular_button.grid(row=4, column=2, columnspan=2, pady=20)

        self.resultado_label.grid(row=5, column=1, columnspan=2, pady=10)
        self.resultado_cal.grid(row=6, column=1, columnspan=2, pady=10)
        self.resultado_cemento.grid(row=7, column=1, columnspan=2, pady=10)
        self.resultado_arena.grid(row=8, column=1, columnspan=2, pady=10)

        self.master.resizable(False, False)


    def set_calcular_command(self, command):
        self.calcular_button.config(command=command)

    def mostrar_resultados(self, cantidad_ladrillos, cantidad_cal, cantidad_cemento, cantidad_arena):
        self.resultado_label.config(text=f"Cantidad de {self.tipo_ladrillo_var.get()}s necesarios: {cantidad_ladrillos}")
        self.resultado_cal.config(text=f"Cantidad de cal necesaria: {cantidad_cal} kg")
        self.resultado_cemento.config(text=f"Cantidad de cemento necesario: {cantidad_cemento} kg")
        self.resultado_arena.config(text=f"Cantidad de arena necesaria: {cantidad_arena} metros cúbicos")
