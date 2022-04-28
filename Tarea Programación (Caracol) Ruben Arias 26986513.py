#Tarea del Caracol Programación
#Algebra usada
#La pared tiene una altura de H metros, el caracol sube Ld metros todos los días y se desliza Ln metros todas las noches
#una vez que el caracol llega a la copa de la pared no me importa mucho si el caracol se desliza en esa noche.
#Por lo tanto, si el caracol necesita x días para llegar a la copa de la pared, se desliza (X-1) veces y sube x veces.
#Supongamos que el caracol tarda X días en llegar a la copa de la pared, entonces:
#Ldx - Ln(x-1) = H
#x = (H - Ln)/(Ld - Ln)

H = float(input("Ingrese la altura de la pared: "))
Ld = float(input("Ingrese los metros que asciende: "))
Ln = float(input("Ingrese los metros que resbala: "))

if H >= Ld and Ld > Ln:
    d = (H - Ln) / (Ld - Ln)
    w=int(d)
    print("El caracol ha tardado ", w, "días en subir")

elif Ld > H:
    print("El caracol ha subido en el primer día")

else:
    print("El caracol sigue bajando toda la noche!!")
