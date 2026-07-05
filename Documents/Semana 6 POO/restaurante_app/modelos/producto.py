class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    """
    
    def __init__(self, nombre, precio, disponible):
        """
        Constructor de la clase Producto.
        """
        self.nombre = nombre
        self.__precio = precio   # Encapsulación: precio es privado
        self.disponible = disponible
    
    def obtener_precio(self):
        """Método para obtener el precio"""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """Método para cambiar el precio con validación"""
        if nuevo_precio <= 0:
            print("Error: El precio debe ser mayor que cero.")
            return False
        self.__precio = nuevo_precio
        print(f"Precio de {self.nombre} actualizado correctamente.")
        return True
    
    def mostrar_informacion(self):
        """Muestra la información básica del producto"""
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Estado: {estado}")