import tkinter as tk
from tkinter import ttk

def calcular_ladrillos():
    try:
        tipo_ladrillo = tipo_ladrillo_var.get()
        altura_ladrillo = tipos_ladrillos[tipo_ladrillo]["altura"]
        largo_ladrillo = tipos_ladrillos[tipo_ladrillo]["largo"]

        altura_pared = float(entry_altura_pared.get())
        largo_pared = float(entry_largo_pared.get())

        superficie_ladrillo = altura_ladrillo * largo_ladrillo
        superficie_pared = altura_pared * largo_pared

        cantidad_ladrillos = superficie_pared / superficie_ladrillo

        resultado_label.config(text=f"Cantidad de {tipo_ladrillo}s necesarios: {round(cantidad_ladrillos)}")

        # Calcular la cantidad de cal, cemento y arena necesarios por metro cuadrado
        cal_por_metro_cuadrado = 7.30  # kg
        cemento_por_metro_cuadrado = 7.50  # kg
        arena_por_metro_cuadrado = 0.035  # metros cúbicos

        cantidad_cal = cal_por_metro_cuadrado * superficie_pared
        cantidad_cemento = cemento_por_metro_cuadrado * superficie_pared
        cantidad_arena = arena_por_metro_cuadrado * superficie_pared

        resultado_cal.config(text=f"Cantidad de cal necesaria: {round(cantidad_cal, 2)} kg")
        resultado_cemento.config(text=f"Cantidad de cemento necesario: {round(cantidad_cemento, 2)} kg")
        resultado_arena.config(text=f"Cantidad de arena necesaria: {round(cantidad_arena, 3)} metros cúbicos")

    except ValueError:
        resultado_label.config(text="Por favor, ingrese valores numéricos.")

# Tipos de ladrillos con medidas predefinidas
tipos_ladrillos = {
    "Ladrillo Comunes 5x25": {"altura": 0.05, "largo": 0.25},
    "Ladrillo Huecos 18x33": {"altura": 0.18, "largo": 0.33},
    "Ladrillo Vista 5x23.5": {"altura": 0.05, "largo": 0.23},
    "Ladrillo Cemento 19x39": {"altura": 0.19, "largo": 0.39},
    "Ladrillo HCCA 25x50": {"altura": 0.25, "largo": 0.50}, 
}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ladrillos")
ventana.geometry("600x600")
ventana.configure(bg="SkyBlue3")

fuente = ("Arial", 12)


# Crear y ubicar los widgets en la ventana
tipo_ladrillo_var = tk.StringVar()

label_tipo_ladrillo = ttk.Label(ventana, text="Tipos de ladrillos:", font=fuente)
tipo_ladrillo_menu = ttk.Combobox(ventana, textvariable=tipo_ladrillo_var, values=list(tipos_ladrillos.keys()), font=fuente)
tipo_ladrillo_menu.set(list(tipos_ladrillos.keys())[0])  # Establecer el valor predeterminado

label_altura_pared = ttk.Label(ventana, text="Altura de la pared (m):", font=fuente, background="")
entry_altura_pared = ttk.Entry(ventana, font=fuente)

label_largo_pared = ttk.Label(ventana, text="Largo de la pared (m):", font=fuente)
entry_largo_pared = ttk.Entry(ventana, font=fuente)

calcular_button = ttk.Button(ventana,  text="Calcular", command=calcular_ladrillos)

resultado_label = ttk.Label(ventana, text="Resultado: ", font=fuente)
resultado_cal = ttk.Label(ventana, text="Cantidad de Cal: ", font=fuente)
resultado_cemento = ttk.Label(ventana, text="Cantidad de Cemento: ", font=fuente)
resultado_arena = ttk.Label(ventana, text="Cantidad de Arena:", font=fuente)

# Ubicar los widgets en la cuadrícula
label_tipo_ladrillo.grid(row=1, column=1, padx=10, pady=30)
tipo_ladrillo_menu.grid(row=1, column=2, padx=10, pady=10)

label_altura_pared.grid(row=2, column=1, padx=10, pady=30)
entry_altura_pared.grid(row=2, column=2, padx=10, pady=10)

label_largo_pared.grid(row=3, column=1, padx=10, pady=30)
entry_largo_pared.grid(row=3, column=2, padx=10, pady=10)

calcular_button.grid(row=4, column=2, columnspan=2, pady=20)

resultado_label.grid(row=5, column=1, columnspan=2, pady=10)
resultado_cal.grid(row=6, column=1, columnspan=2, pady=10)
resultado_cemento.grid(row=7, column=1, columnspan=2, pady=10)
resultado_arena.grid(row=8, column=1, columnspan=2, pady=10)
ventana.resizable(False, False)
# Iniciar el bucle principal de la ventana
ventana.mainloop()