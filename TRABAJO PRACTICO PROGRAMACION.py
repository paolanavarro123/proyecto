#Ejercicios de programacion

#EJERCICIO N1
while True:
    letra1 = input("Ingrese la primera letra: ").lower()
    letra2 = input("Ingrese la segunda letra: ").lower()

    if letra1 == letra2:
        print("Las letras ingresadas son iguales.")
        
    
    else:
        print("Las letras ingresadas son diferentes.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break.

# EJERCICIO N 2
while True:
    palabra1 = input("Ingrese la primera palabra: ").lower()
    palabra2 = input("Ingrese la segunda palabra: ").lower()

    if palabra1 == palabra2:
        print("Las palabras ingresadas son iguales.")
    else:
        print("Las palabras ingresadas son diferentes.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break

#EJERCICIO N 3
while True:
    genero = input("Ingrese su género ('f' para femenino, 'm' para masculino): ").lower()

    if genero == 'f':
        print("Votará en una mesa femenina.")
    elif genero == 'm':
        print("Votará en una mesa masculina.")
    else:
        print("Género no válido. Por favor, ingrese 'f' o 'm'.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break
#EJERCICIO N 4
while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if num1 > num2:
        print("El primer número es mayor.")
    elif num2 > num1:
        print("El segundo número es mayor.")
    else:
        print("Ambos números son iguales.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break


while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if num1 > num2:
        print("El primer número es mayor.")
    elif num2 > num1:
        print("El segundo número es mayor.")
    else:
        print("Ambos números son iguales.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break


#EJERCICIO N 5

 def pesos_a_dolares(cantidad):
    return cantidad / 20

def dolares_a_pesos(cantidad):
    return cantidad * 20

while True:
    print("1. Pesos a Dólares")
    print("2. Dólares a Pesos")
    opcion = input("Seleccione el tipo de cambio (1 o 2): ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad en pesos: "))
        resultado = pesos_a_dolares(cantidad)
        print(f"{cantidad} pesos equivale a {resultado} dólares.")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad en dólares: "))
        resultado = dolares_a_pesos(cantidad)
        print(f"{cantidad} dólares equivale a {resultado} pesos.")
    else:
        print("Opción inválida. Intente nuevamente.")

    opcion = input("¿Desea realizar otra conversión? (s/n): ").lower()
    if opcion != 's':
        break

#EJERCICIO N 6
 while True:
    edad = int(input("Ingrese su edad: "))

    if edad > 16:
        print("Puede votar.")
    else:
        print("No puede votar.")

    opcion = input("¿Desea realizar otra verificación? (s/n): ").lower()
    if opcion != 's':
        break


# ESTRUCTURA CONDICIONAL COMPUESTA ( IF ANIDADOS)

#EJERCICIO N 1

while True:
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

    opcion = input("¿Desea ingresar otro triángulo? (s/n): ").lower()
    if opcion != 's':
        break

#EJERCICIO N2

 while True:
    importe = float(input("Ingrese el importe a pagar: "))
    forma_pago = int(input("Seleccione la forma de pago:\n1. Contado\n2. Tarjeta\n3. Débito\n"))

    if forma_pago == 1:
        descuento = importe * 0.1  # 10% de descuento
        importe_total = importe - descuento
        print("Importe: $", importe)
        print("Descuento: $", descuento)
        print("Importe total: $", importe_total)
    elif forma_pago == 2:
        interes = importe * 0.1  # 10% de interés
        importe_total = importe + interes
        print("Importe: $", importe)
        print("Interés: $", interes)
        print("Importe total: $", importe_total)
    elif forma_pago == 3:
        descuento = importe * 0.05  # 5% de descuento
        importe_total = importe - descuento
        print("Importe: $", importe)
        print("Descuento: $", descuento)
        print("Importe total: $", importe_total)
    else:
        print("Forma de pago no válida. Intente nuevamente.")

    opcion = input("¿Desea realizar otro pago? (s/n): ")
    if opcion.lower() != 's':
        break

#EJERCICIO N 3

: while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    mayor = max(num1, num2, num3)

    print("El número mayor es:", mayor)

    if mayor % 2 == 0:
        print("El número mayor es par.")
    else:
        print("El número mayor es impar.")

    opcion = input("¿Desea ingresar otros tres números? (s/n): ")
    if opcion.lower() != 's':
        break

#EJERCICIO N 4


 while True:
    numero = int(input("Ingrese un número del 1 al 7: "))

    if numero == 1:
        print("El número corresponde al día Lunes.")
    elif numero == 2:
        print("El número corresponde al día Martes.")
    elif numero == 3:
        print("El número corresponde al día Miércoles.")
    elif numero == 4:
        print("El número corresponde al día Jueves.")
    elif numero == 5:
        print("El número corresponde al día Viernes.")
    elif numero == 6:
        print("El número corresponde al día Sábado.")
    elif numero == 7:
        print("El número corresponde al día Domingo.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 7.")

    opcion = input("¿Desea ingresar otro número? (s/n): ")
    if opcion.lower() != 's':
        break

#EJERCICIO N 5

while True:
    numero = int(input("Ingrese un número del 1 al 12: "))

    if numero == 1:
        print("El número corresponde al mes de Enero.")
    elif numero == 2:
        print("El número corresponde al mes de Febrero.")
    elif numero == 3:
        print("El número corresponde al mes de Marzo.")
    elif numero == 4:
        print("El número corresponde al mes de Abril.")
    elif numero == 5:
        print("El número corresponde al mes de Mayo.")
    elif numero == 6:
        print("El número corresponde al mes de Junio.")
    elif numero == 7:
        print("El número corresponde al mes de Julio.")
    elif numero == 8:
        print("El número corresponde al mes de Agosto.")
    elif numero == 9:
        print("El número corresponde al mes de Septiembre.")
    elif numero == 10:
        print("El número corresponde al mes de Octubre.")
    elif numero == 11:
        print("El número corresponde al mes de Noviembre.")
    elif numero == 12:
        print("El número corresponde al mes de Diciembre.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 12.")

    opcion = input("¿Desea ingresar otro número? (s/n): ")
    if opcion.lower() != 's':
        break
