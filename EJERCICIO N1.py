
    #Ejercicio N1
("Ingrese 4 numeros")
par=0;impar=0;total=0
for i in range (4):
n = int(input(f" Ingrese el {i+1}ro numeros:"))
if(n%2==0):
par +=1
total+=n
else:
impar +=1
print(f"Hay{par}numeros pares, {impar} la suma de todos los pares es de {total}") 
    