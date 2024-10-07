

inventario = []
# Debajo voy a crear todas las funciones que tiene el menú principal. Y debajo una función main que contendrá if y elif sobre las funciones elegidas y se invocaran las funciones mostrando la lista de productos.

# Menú principal

def menuPrincipal ():    
    print("Bienvenido al menu principal")
    print("0. Mostrar Lista (Debugging)")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto más caro y más barato")
    print("5. Mostrar productos con precio mayor a 15000")
    print("6. Salir")

# Cargar un producto a la lista

def cargarProducto(inventario):
    n = int(input("Cuantos productos desea agregar?: "))
    for _ in range (n):
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        inventario.append([nombre, precio, cantidad])

# Buscar un producto de la lista (si fue previamente añadido), uso .lower para facilitar el debugging y el uso de las opciones asi se ahorra tiempo.

def buscarProducto(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    nombre_buscar = input("Nombre del producto a buscar: ")
    for producto in inventario:
        if len(producto) < 3:
            print("Error: Producto mal formado en el inventario.")
            continue
        if producto[0].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
            return
    print("Producto no encontrado.")


# Organizar inventario ascendentemente

# La función obtener precio es para almacenar la lista ya creada anteriormente. (igual la voy a usar en varios puntos :D).

def obtenerPrecio(producto):
    return producto[1]

def ordenarInventario(inventario):
    inventario.sort(key=obtenerPrecio)
    print("Inventario ordenado por precio:")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")

# Mostrar producto mas barato y mas caro.

def mostrarProductoMasCaroYMasBarato(inventario):
    productoMasCaro = max(inventario, key=obtenerPrecio)
    productoMasBarato = min(inventario, key=obtenerPrecio)
    print(f"Producto más caro: Nombre: {productoMasCaro[0]}, Precio: {productoMasCaro[1]}, Cantidad: {productoMasCaro[2]}")
    print(f"Producto más barato: Nombre: {productoMasBarato[0]}, Precio: {productoMasBarato[1]}, Cantidad: {productoMasBarato[2]}")

    producto_mas_barato = min(inventario, key=obtenerPrecio)
    print(f"Producto más barato: Nombre: {producto_mas_barato[0]}, Precio: {producto_mas_barato[1]}, Cantidad: {producto_mas_barato[2]}")

# Mostrar producto con precio mayor a 15000

def mostrarProductosMayorQuinceMil(inventario):
    productosCaros = [producto for producto in inventario if producto[1] > 15000]
    if productosCaros:
        print("Productos con precio mayor a 15000:")
        for producto in productosCaros:
            print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
    else:
        print("No hay productos con precio mayor a 15000.")


# Función principal que ejecuta funciones en base a las opciones elegidas en el menú.

def main():
    while True:
        menuPrincipal()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            cargarProducto(inventario)
            print("Inventario cargado:")
            for producto in inventario:
                print(producto)
        elif opcion == "2":
            if not inventario:
                print("No hay productos disponibles para la operación solicitada.")
            else:
                buscarProducto(inventario)
        elif opcion == "3":
            if not inventario:
                print("No hay productos disponibles para la operación solicitada.")
            else:
                ordenarInventario(inventario)
        elif opcion == "4":
            if not inventario:
                print("No hay productos disponibles para la operación solicitada.")
            else:
                mostrarProductoMasCaroYMasBarato(inventario)
        elif opcion == "5":
            if not inventario:
                print("No hay productos disponibles para la operación solicitada.")
            else:
                mostrarProductosMayorQuinceMil(inventario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# se ejecuta esto para que apenas se ejecute el codigo aparezca el menú principal (esto se lo pregunté a don google :P por que no me daba el bocho para hacer q se ejecute todo al inicio jeje, obviamente en el parcial no lo voy a hacer )

if __name__ == "__main__":
    main()
    
    