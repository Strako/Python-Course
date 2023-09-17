class Empleado:
    def __init__(self, nombre, puesto, antiguedad):
        self.nombre = nombre
        self.puesto = puesto
        self.antiguedad = antiguedad
    
    def __str__(self):
        return f"{self.nombre}, Puesto: {self.puesto}, Antigüedad: {self.antiguedad} años"
    
    def __str__(self):
        return f"{self.nombre}, Puesto: {self.puesto}, Antigüedad: {self.antiguedad} años"
    
    def ascender(self, nuevo_puesto):
        self.puesto = nuevo_puesto

    def obtener_antiguedad(self, nuevo_puesto):
        self.puesto = nuevo_puesto

    def aumentar_antiguedad(self, anios):
        self.antiguedad += anios

    


empleado1 = Empleado("Jose Nah", "Backend Developer", 3)
empleado1.aumentar_antiguedad(2)
print(empleado1)
    