positivo=[]
negativo=[]
for i in range(15):
    n=int(input(f"Ingresar el ¨{i+1}ºnúmero negativo:"))
    negativo.append(n)
    for num in negativo:
        positivo.append(abs(num))
        print(f"Estos son los numeros en positivo¨{positivo}")