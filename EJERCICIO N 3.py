M=0; F=0
mayor=0;menor=0
print("Ingresar el sexo(M/F)y la edad")
for i in range(15):
    print(f"¨{i+1}ºPersona")
    sexo=input("Sexo:")
    edad=int(input("Edad:"))
    if(sexo.upper()=="M"):
        M+=1
    else:
        menor+=1
        print(f"Hay¨{M}Masculinos,¨{F}Femeninos y ¨{mayor}son mayores,{menor}son menores")+
        