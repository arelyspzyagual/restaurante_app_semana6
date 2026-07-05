# Sistema de Gestión de Restaurante - POO

El sistema permite registrar **platillos** y **bebidas** de un restaurante mediante un menú por consola. Su propósito principal es demostrar cómo aplicar correctamente los principios de herencia, encapsulación y polimorfismo tal enseñados en clases.

## Objetivos de aprendizaje

Durante el desarrollo de este proyecto se aplican los siguientes conceptos:

Definición de clases y objetos
Uso del constructor `__init__()`
Herencia entre clases
Encapsulación de atributos
Polimorfismo
Organización modular del proyecto

## Estructura del proyecto
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

## Nota del estudiante: Por alguna razón en mi codigo, la sección de producto terminó abajo de los demas, no lo puedo cambiar, así que el orden de mi estructura es diferente al que pidieron.  

## Modelos

La carpeta **modelos** contiene las clases que representan las entidades principales:

**Producto:** Clase padre
**Platillo:** Hereda de Producto
**Bebida:** Hereda de Producto

## Servicios

La carpeta **servicios** contiene la lógica principal del sistema.

La clase **Restaurante** administra los productos registrados durante la ejecución del programa.

## Punto de entrada

El archivo **main.py** es el punto de inicio del programa. Desde aquí se muestra el menú interactivo, se registran los productos y se demuestra el polimorfismo.


### Encapsulación

El atributo `__precio` en la clase `Producto` está encapsulado. Se accede y modifica mediante los métodos:
`obtener_precio()`
`cambiar_precio()`

### Polimorfismo

Tanto `Platillo` como `Bebida` sobrescriben el método `mostrar_informacion()`. Al recorrer la lista de productos, cada uno muestra su información de forma diferente.

## Conclusión

Este proyecto representa un importante paso en mi aprendizaje de la Programación Orientada a Objetos. A través del desarrollo del Sistema de Gestión de Restaurante, pude aplicar de manera práctica los tres pilares fundamentales de la POO: herencia, encapsulación y polimorfismo.
La herencia me permitió crear una estructura lógica y eficiente mediante la clase padre Producto y las clases hijas Platillo y Bebida, reutilizando código y evitando redundancias. La encapsulación del atributo __precio me ayudó a entender la importancia de proteger los datos internos de las clases y controlar su acceso mediante métodos específicos. Finalmente, el polimorfismo quedó demostrado claramente al sobrescribir el método mostrar_informacion() en las clases hijas, permitiendo que un mismo mensaje produjera resultados diferentes según el tipo de producto.
Aunque inicialmente me guie en el ejemplo del docente (sistema de biblioteca), logré adaptar los conceptos al contexto de un restaurante, para intentar cumplir con los requerimientos de la actividad. Este proceso me enseñó que los principios de la POO no solo sirven para resolver problemas técnicos, sino que ayudan a crear código más organizado, mantenible y escalable.
Sin duda, esta experiencia reforzó mi comprensión sobre cómo estructurar proyectos de forma modular y cómo pensar en términos de objetos y responsabilidades. Estoy convencido de que estos conocimientos serán fundamentales para enfrentar proyectos más complejos en el futuro.

## Autor

**Arelys Pezo Yagual**