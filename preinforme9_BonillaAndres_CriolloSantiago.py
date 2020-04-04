#Ejercicio 1

'''x1=float(input("Ingresar x del primer punto: "))
y1=float(input("Ingresar y del primer punto: "))
x2=float(input("Ingresar x del segundo punto: "))
y2=float(input("Ingresar y del segundo punto: "))

distancia_euclidiana=((x2-x1)**2+(y2-y1)**2)**(1/2)

print(distancia_euclidiana)'''

#Ejercicio 2

'''def inverso(num):
    div=10
    num2=0
    while num!=0:
        resta=num%div
        num=num-resta
        num2=(num2*10+resta/div)
        div=div*10
    num2=int(num2*10)
    return num2

num=int(input("Digite el numero: "))
num2=inverso(num)
print(num2)'''

#Ejercicio 3

'''nota1=float(input("Digite la primer nota: "))
nota2=float(input("Digite la segunda nota: "))
nota3=float(input("Digite la tercera nota: "))
nota4=float(input("Digite la cuarta nota: "))
nota5=float(input("Digite la quinta nota: "))

nota_final=(nota1*0.15)+(nota2*0.2)+(nota3*0.15)+(nota4*0.3)+(nota5*0.2)

if nota_final<2.0:
    print("El estudiante no puede habilitar")
elif nota_final<3.0:
    print("El estudiante reprobo")
elif nota_final>=3.0 and nota_final<=4.5:
    print("El estudiante aprobo")
elif nota_final>4.5:
    print("Felicitaciones querido estudiante")'''

#Ejercicio 4

numero_fila=int(input("Digite el numero de filas"))
secuencia=0
mult=10
for i in range(1,numero_fila+1):
    secuencia=(secuencia*mult)+i
    if i==9:
        mult=100
    print(secuencia)
