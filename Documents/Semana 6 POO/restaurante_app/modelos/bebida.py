from modelos.producto import Producto

class Bebida(Producto):
    """
    Clase hija que representa una bebida del restaurante.
    Hereda de la clase Producto.
    """
    
    def __init__(self, nombre, precio, volumen_ml, tipo_bebida="Refresco", disponible=True):
        """
        Constructor de la clase Bebida.
        Usa super() para reutilizar el constructor de Producto.
        """
        super().__init__(nombre, precio, disponible)
        
        # Atributos propios de la bebida
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida   # Ej: Refresco, Jugo, Alcohólica
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre.
        Demuestra polimorfismo.
        """
        super().mostrar_informacion()   # Llama al método del padre
        print(f"Tipo de bebida: {self.tipo_bebida}")
        print(f"Volumen: {self.volumen_ml} ml")
        print("-" * 40)