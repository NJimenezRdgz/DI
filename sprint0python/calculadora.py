from operaciones import suma, resta, multiplicacion, division


respuesta = 's'


while respuesta == 's':
    print("Dame 2 valores")

    # Solicita al usuario que ingrese dos valores
    a = int(input("Valor a: "))
    b = int(input("Valor b: "))

    # Solicita al usuario que seleccione una operación
    operacion = input("Selecciona una acción a realizar (suma, resta, multiplicacion, division): ")

    # Ejecuta la operación seleccionada y muestra el resultado
    if operacion == 'suma':
        print(suma(a, b))
    elif operacion == 'resta':
        print(resta(a, b))
    elif operacion == 'multiplicacion':
        print(multiplicacion(a, b))
    elif operacion == 'division':
        print(division(a, b))
    else:
        # Mensaje de error si la operación no es válida
        print("No has seleccionado una acción válida")

    # Pregunta al usuario si desea realizar más operaciones
    respuesta = input("¿Quieres hacer más operaciones? (s=si//n=no): ")
