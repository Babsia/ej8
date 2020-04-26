from claseconjunto import conjunto
from manejadorconjuntos import manejador
def opcion0():
    print("Adiós")

def opcion1():
    i1=int(input("ingrese el numero de conjunto a unir: "))
    i2=int(input("ingrese el segundo numero de conjunto a unir: "))
    i1-=1
    i2-=1
    f=l.manejadorunion(i1,i2)
    f.mostrar()

def opcion2():
    i1=int(input("ingrese el numero de conjunto: "))
    i2=int(input("ingrese el segundo numero de conjunto de diferencia: "))
    i1-=1
    i2-=1
    h=l.manejadordif(i1,i2)
    h.mostrar()

def opcion3():
    i1=int(input("ingrese el numero de conjunto: "))
    i2=int(input("ingrese el segundo numero de conjunto de diferencia: "))
    i1-=1
    i2-=1
    t=l.manejadoreq(i1,i2)
    if (t==True):
        print("los conuntos son iguales")
    else:
        print("los conjuntos son distintos")



switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    l=manejador()
    l.testing()
    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Union 1")
        print("2 Diferencia 2")
        print("3 Igualdad 3")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 