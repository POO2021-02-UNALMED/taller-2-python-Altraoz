class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
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
        a = "Las piezas no son originales"
        b = "Auto original"
        for asiento in self.asientos:
            if asiento!=None:
                if(asiento.registro!=self.registro or asiento.registro!=self.motor.registro):
                   return a

        return b

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
