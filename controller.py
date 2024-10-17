# controller.py

from model import Ladrillo
from view import Vista
import tkinter as tk

class Controlador:
    def __init__(self, root):
        self.vista = Vista(root)
        self.vista.set_calcular_command(self.calcular_ladrillos)
        #resetear
        self.vista.set_reset_comand(self.resetear_campos)

    def calcular_ladrillos(self):
        try:
            tipo_ladrillo = self.vista.tipo_ladrillo_var.get()
            altura_pared = float(self.vista.entry_altura_pared.get())
            largo_pared = float(self.vista.entry_largo_pared.get())

            cantidad_ladrillos = Ladrillo.calcular_cantidad_ladrillos(tipo_ladrillo, altura_pared, largo_pared)
            superficie_pared = altura_pared * largo_pared
            cantidad_cal, cantidad_cemento, cantidad_arena = Ladrillo.calcular_materiales(superficie_pared)

            self.vista.mostrar_resultados(cantidad_ladrillos, cantidad_cal, cantidad_cemento, cantidad_arena)

        except ValueError:
            self.vista.resultado_label.config(text="Por favor, ingrese valores numéricos.")
    #limpiar campos
    def resetear_campos(self):
        self.vista.limpiar_campos()

if __name__ == "__main__":
    root = tk.Tk()
    app = Controlador(root)
    root.mainloop()
