from datetime import date
#imprimir
""""
print('today is: '+ str(date.today()))

print('suma de numeros')
num1=input('ingresa el primer numero')
num2=input('ingresa el segundo numero')
print(int(num1)+int(num2))
 
"""

#arreglos
"""
nombre=["ian", "ZAna", "Raul"]
print(nombre)
print(nombre[0])
nombre.append("New")
print(nombre)
nombre.insert(0,"Ali")
print("Lista con Ali en primera pos",nombre)
nombre.remove("Raul")
print("\n Lista sin Raul", nombre)
nombre.pop(1)
print("\n Lista con pos 1 eliminada",nombre)
nombre.sort()
print("\n lista ordenada",nombre)
nombre.reverse()
print("\n Lista en orden al revez",nombre)
"""
#Tuplas
"""
MiTupla=(1,2,3,8,2,3,2)
print(MiTupla)
print("El numero 2 aparece ",MiTupla.count(2),"veces")

print("El numero 2 aparece por primera vez en la posicion ",MiTupla.index(2))
print("El numero 2 aparece por primera vez en la posicion ",MiTupla.index(2,2),"Buscando a partir de la posicion 2")
print("El numero 3 aparece por primera vez en la posicion ",MiTupla.index(3,3,6),"buscando a partir de las pos 3")
print("La tupla tiene",len(MiTupla), "elementos")
"""
#Dictionaries
"""""
alguien={"name":"Alan", "edad":"25", "pais":"Mexico"}
print("Mi pais es",alguien["pais"])
print("los datos solicitados son:",alguien.keys(), "los datos que di fueron",alguien.values())
extras={"ocupacion":"Maestro","año":"2000"}
alguien.update(extras)
print("la informacion completa es ", alguien.items())
alguien.update({"hobby":"pescar"})
print("creo que puedo añadrie informacion extra con ",alguien.items())
"""
#SETS

Primerset={1,2,3}
segundoSet=set([3,4,5,6])
#operaciones con conjuntos
union=Primerset | segundoSet
#print(Primerset)
#print(segundoSet)
#print("la union de los conjuntos es", union)
#print("La interseccion de los conjuntos es", Primerset&segundoSet)
#print("La diferencia simetrica o los conjuntos no compartidos es", Primerset^segundoSet)
#metodos
segundoSet.add(8)
#print(segundoSet)
Primerset.remove(1)
#print(Primerset)


#Funciones

def sumar(a,b):
    #print(f"la sumas ee, {a+b}")
    return a+b
sumando=sumar(3,78)
#print(f"si guardarmos una varible a retornar aqui se imprime{sumando}")

#manejo de excepciones

def dividir(x,y):
    try:
        x/y
       # return x/y
    except(ZeroDivisionError):
        print("Error, se esta dividiendo por cero")
    except(TypeError):
        print("Error, Introduce solo numeros")
    else:
        print(f"el resultado es",x/y)
    finally:
        print("Tarea terminada")

print(dividir(12,2))
