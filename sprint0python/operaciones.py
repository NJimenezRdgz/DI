def suma(a, b):
    # Devuelve la suma de a y b
    return a + b

def resta(a, b):
    # Devuelve la resta de a menos b
    return a - b

def multiplicacion(a, b):
    # Devuelve el producto de a y b
    return a * b

def division(a, b):
    # Comprueba si b es cero antes de realizar la división
    if b == 0:
        # Muestra un mensaje de error si b es cero
        return print("No se puede dividir entre 0")
    else:
        # Devuelve el resultado de la división de a entre b
        return a / b
