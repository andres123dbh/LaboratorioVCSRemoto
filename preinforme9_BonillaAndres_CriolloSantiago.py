#Ejercicio 1

'''x1=float(input("Ingresar x del primer punto: "))
y1=float(input("Ingresar y del primer punto: "))
x2=float(input("Ingresar x del segundo punto: "))
y2=float(input("Ingresar y del segundo punto: "))

distancia_euclidiana=((x2-x1)**2+(y2-y1)**2)**(1/2)

print(distancia_euclidiana)'''

#Ejercicio 2

def inverso(num):
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
print(num2)