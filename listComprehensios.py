x = int(input("valor para i= "))
y = int(input("valor para j= "))
z = int(input("valor para k= "))
n = int(input("valor para n= "))
#n = int(input())
def guardar(eje):
    """
    Guarda las coordenadas posibles para cada eje de 0 a el numero ingresado por el usuario
    Args:
        eje: corresponde a x, y o Z segun sea el caso
    """
    posibilidades=[posibilidad+1 for posibilidad in range(-1, eje) if posibilidad<=eje]
    return posibilidades
i=guardar(x)
j=guardar(y)
k=guardar(z)
#print(i,j,k)                       
coordenada=[[a,b,c] for a in range (0, len(i))
            for b in range (0, len(j))
            for c in range (0, len(k)) if i[a]+j[b]+k[c] != n]
resultado=list(coordenada)
print(resultado)

    
