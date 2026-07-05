from modelos.producto import Producto

class Restaurante:
    """
    Clase de servicio que administra los productos del restaurante.
    Similar al estilo del ejemplo de Biblioteca del docente.
    """
    def __init__(self):
        self.productos = []  # Lista de productos (Platillo y Bebida)

    def registrar_producto(self, producto):
        """Registra un producto (Platillo o Bebida) en el restaurante"""
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"\nProducto '{producto.nombre}' registrado correctamente.")
        else:
            print("\nError: Solo se pueden registrar productos.")

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.
        Aquí se demuestra el polimorfismo.
        """
        print("\n" + "="*50)
        print("          PRODUCTOS DEL RESTAURANTE")
        print("="*50)
        
        if not self.productos:
            print("No existen productos registrados.")
            return
        
        print("\nDemostración del polimorfismo:\n")
        for producto in self.productos:
            producto.mostrar_informacion()
            print("-" * 50)