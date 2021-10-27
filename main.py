class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.regitro = registro
    
    def cambiarColor(self, color):
        if (color == "rojo" or color =="verde" or color =="amarillo" or color =="negro" or color =="blanco"):
            self.color = color
    
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        total_Asientos = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                total_Asientos = total_Asientos + 1
        return total_Asientos
    
    def verificarIntegridad(self):
        estado = True
        if self.motor.registro == self.registro:
            for j in self.asientos:
                if (not (isinstance (j, Asiento) and j.registro == self.registro)):
                    estado = False
            if estado:
                print("Auto original")
            else:
                print("Las piezas no son originales")

class Motor:
    def __init__ (self, numeroCilindros, tipo, regitro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = regitro
    
    def cambiarRegistro (self, r):
        self.registro = r
    
    def asignarTipo(self, tipo):
        if tipo =="normal" or tipo == "electrico":
            self.tipo = tipo
