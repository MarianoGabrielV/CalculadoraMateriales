# model.py

class Ladrillo:
    tipos_ladrillos = {
        "Ladrillo Comunes 5x25": {"altura": 0.05, "largo": 0.25},
        "Ladrillo Huecos 18x33": {"altura": 0.18, "largo": 0.33},
        "Ladrillo Vista 5x23.5": {"altura": 0.05, "largo": 0.23},
        "Ladrillo Cemento 19x39": {"altura": 0.19, "largo": 0.39},
        "Ladrillo HCCA 25x50": {"altura": 0.25, "largo": 0.50},
    }

    @classmethod
    def calcular_cantidad_ladrillos(cls, tipo_ladrillo, altura_pared, largo_pared):
        altura_ladrillo = cls.tipos_ladrillos[tipo_ladrillo]["altura"]
        largo_ladrillo = cls.tipos_ladrillos[tipo_ladrillo]["largo"]

        superficie_ladrillo = altura_ladrillo * largo_ladrillo
        superficie_pared = altura_pared * largo_pared

        cantidad_ladrillos = superficie_pared / superficie_ladrillo

        return round(cantidad_ladrillos)

    @staticmethod
    def calcular_materiales(superficie_pared):
        cal_por_metro_cuadrado = 7.30  # kg
        cemento_por_metro_cuadrado = 7.50  # kg
        arena_por_metro_cuadrado = 0.035  # metros cúbicos

        cantidad_cal = cal_por_metro_cuadrado * superficie_pared
        cantidad_cemento = cemento_por_metro_cuadrado * superficie_pared
        cantidad_arena = arena_por_metro_cuadrado * superficie_pared

        return round(cantidad_cal, 2), round(cantidad_cemento, 2), round(cantidad_arena, 3)
