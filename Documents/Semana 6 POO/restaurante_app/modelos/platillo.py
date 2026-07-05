from modelos.producto import Producto

class Platillo(Producto):
    """
    Clase hija que representa un platillo del restaurante.
    Hereda de la clase Producto.
    """
    
    def __init__(self, nombre, precio, calorias, tipo="Principal", disponible=True):
        """
        Constructor de la clase Platillo.
        Usa super() para reutilizar el constructor de Producto.
        """
        super().__init__(nombre, precio, disponible)
        
        # Atributos propios del platillo
        self.calorias = calorias
        self.tipo = tipo   # Ej: Entrada, Principal, Postre
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre.
        Demuestra polimorfismo.
        """
        super().mostrar_informacion()   # Llama al método del padre
        print(f"Tipo de platillo: {self.tipo}")
        print(f"Calorías: {self.calorias} kcal")
        print("-" * 40)