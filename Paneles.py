#x ancho, y alto
#b ancho, a alto
import math
def cuantos_paneles_caben(a, b, x, y):
    if b > x or a > y:
        return 0
    else:
        # Cuantos paneles(a,b) caben en X e Y
        paneles_Y= math.trunc(y / a) 
        paneles_X = math.trunc(x / b) 

        paneles_totales = paneles_Y * paneles_X

        # x menos la cantidad de espacios que se utilizaron en X 
        restantes_X = x - (paneles_X * b)

        # Si sobran espacios
        if restantes_X > 0:
            # los espacios sobrantes en el eje Y
            restantes_Y = paneles_Y * a

            # Se divide la cantidad de espacios sobrantes en el eje Y, con la cantidad de espacios que se pueden utilizar con b
            paneles_Y_extra = math.trunc(restantes_Y/(paneles_X * b))
            paneles_totales += paneles_Y_extra
            
            return paneles_totales
        else:
            return paneles_totales
resultado1 = cuantos_paneles_caben(1,2,3,5) #7
print(resultado1)
resultado2 = cuantos_paneles_caben(1,2,2,4) #4
print(resultado2)
resultado3 = cuantos_paneles_caben(2,2,1,10)#0
print(resultado3)
resultado4 = cuantos_paneles_caben(4,1,8,5) #8
print(resultado4)
