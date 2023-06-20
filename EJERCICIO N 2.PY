#EJERCICIO N 2
mayor = 0
menor = 0
maximo = float('-inf')
minimo = float('inf')

for i in range(10):
    numero = int(input(f"Ingrese el {i+1}° número: "))
    
    if numero > 100:
        mayor += 1
    else:
        menor += 1
    
    if numero > maximo:
        maximo = numero
    
    if numero < minimo:
        minimo = numero

print(f"Cantidad de números mayores a 100: {mayor}")
print(f"Cantidad de números menores a 100: {menor}")
print(f"Número máximo: {maximo}")
print(f"Número mínimo: {minimo}")


