from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "="*50)
    print("     SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*50)
    print("1. Registrar Platillo")
    print("2. Registrar Bebida")
    print("3. Mostrar productos")
    print("4. Salir")
    print("="*50)

def registrar_platillo(restaurante):
    print("\n=== REGISTRAR PLATILLO ===")
    nombre = input("Nombre del platillo: ")
    precio = float(input("Precio ($): "))
    calorias = int(input("Calorías: "))
    tipo = input("Tipo (Entrada, Principal, Postre, etc): ")
    
    platillo = Platillo(nombre, precio, calorias, tipo)
    restaurante.registrar_producto(platillo)

def registrar_bebida(restaurante):
    print("\n=== REGISTRAR BEBIDA ===")
    nombre = input("Nombre de la bebida: ")
    precio = float(input("Precio ($): "))
    volumen = int(input("Volumen (ml): "))
    tipo = input("Tipo (Refresco, Natural, Alcohólica, etc): ")
    
    bebida = Bebida(nombre, precio, volumen, tipo)
    restaurante.registrar_producto(bebida)

def main():
    restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_platillo(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            restaurante.mostrar_productos()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de restaurante!")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()