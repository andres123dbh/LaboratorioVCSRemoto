#a=float(input("Digite el primer numero: "))
#c=float(input("Digitar el segundo numero: "))
#b=int(input("Digitar el tercer numero: "))
#d=float(input("Digitar el cuarto numero: "))
#print("El producto es: ",a*c)
#print("El doble del primer numero es: ",a*2)
#print("El cuadrado del tercer numero es: ",b**2)
#print("La raiz del cuarto numero es: ",d*(1/2))
a=float(input("Digite el a numero: "))
b=float(input("Digitar el b numero: "))
c=float(input("Digitar el c numero: "))
d=(b**2)-4*a*c
if d>0:
    x1=(-b+(d**(1/2)))/(2*a)
    x2=(-b-(d**(1/2)))/(2*a)
    print("Tiene dos soluciones distantes las cuales son ",x1," y ",x2)
elif d==0:
    print("x1 y x2 son iguales y corresponden a: ",-b/(2*a))
elif d<0:
    print("No existe solución de la ecuación cuadrática dentro del dominio de los números reales")

