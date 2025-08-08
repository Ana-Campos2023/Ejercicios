def sorter(n):
    """
    define si un numero es mpar o esta en determinado rango
        args:
            n el numero a calificar
        return:
                no hay datos devueltos, solo se imprime el mensaje requerido
    """
    if n%2!=0:
        print("Weird")
    elif n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
sorter(int(input()))
