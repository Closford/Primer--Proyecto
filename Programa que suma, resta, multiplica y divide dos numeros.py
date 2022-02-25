#Programa que resta dos numeros
print("Introducir los numeros que va a utilizar para las operaciones ")
numero1 = int(input("Indroducir un número : "))
numero2 = int(input("Indroducir otro número : "))
operacion =input("suma, resta, división, multiplicación: ")

if operacion == "suma":
    print("La suma entre ambos numeros es: ", (numero1+numero2))
elif operacion == "resta":
    print("La resta entre ambos numeros es: ", (numero1-numero2))
elif operacion == "división":
    print("La division entre ambos numeros es: ", (numero1/numero2))
elif operacion == "mutiplicacion":
    print("La multiplicacion entre ambos numeros es: ", (numero1*numero2))
