

print("Dame 2 valores")
a = int(input("Valor a: "))
b = int(input("Valor b: "))
operacion = input("Selecciona una accion a realizar(suma, resta, multiplicacion, division): ")

if operacion == 'suma':

    print(a+b)
elif operacion == 'resta':
    print(a-b)
elif operacion == 'multiplicacion':
    print(a*b)
elif operacion == 'division':
    if b == 0:
        print("No se puede dividir entre 0")
    else:
        print(a/b)
else:
    print("No has seleccionado una accion valida")