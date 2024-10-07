from operaciones import suma, resta, multiplicacion,division
respuesta = 's'
while(respuesta == 's'):
    print("Dame 2 valores")
    a = int(input("Valor a: "))
    b = int(input("Valor b: "))
    operacion = input("Selecciona una accion a realizar(suma, resta, multiplicacion, division): ")

    
    if operacion == 'suma':
        print(suma(a,b))
    elif operacion == 'resta':
        print(resta(a,b))
    elif operacion == 'multiplicacion':
        print(multiplicacion(a,b))
    elif operacion == 'division':
        print(division(a,b))
    else:
        print("No has seleccionado una accion valida")
    respuesta = input("Quieres hacer mas operaciones?(s=si//n=no): ")