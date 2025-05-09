def menu():
    print("\n\tCafe y delicias\n")
    print("1. Cafes calientes")
    print("2. Cafes frios")
    print("3. Delicias de sal")
    print("4. delicias de dulce")
    print("5. Salir")
    op=int(input("por favor, seleccione una opcion: "))
    return op

def calientes():
    c=0
    u=0
    p=0
    print("\n\tCafes calientes\n")
    print("1. Expresso...............$2.00")   
    print("2. Capuccino..............$1.50")
    print("3. Americano..............$1.00")
    c=int(input("por favor, seleccione una opcion: "))
    u=int(input("cuantas unidades desea?: "))
    if c==1:
        p=2.00
    elif c==2:
        p=1.50
    elif c==3:
        p=1.00
    return u, p*u

def frios():
    c=0
    u=0
    p=0
    print("\n\tCafes frios\n")
    print("1. Expresso...............$2.00")   
    print("2. Cafe con leche..............$1.50")
    print("3. Cafe frio..............$1.00")
    c=int(input("por favor, seleccione una opcion: "))
    u=int(input("cuantas unidades desea?: "))
    if c==1:
        p=2.00
    elif c==2:
        p=1.50
    elif c==3:
        p=1.00
    return u, p*u

def sal():
    c=0
    u=0
    p=0
    print("\n\tDelicias de sal\n")
    print("1. Sandwich...............$5.00")   
    print("2. Pan con pollo..............$6.50")
    print("3. Pan con jamon..............$5.00")
    c=int(input("por favor, seleccione una opcion: "))
    u=int(input("cuantas unidades desea?: "))
    if c==1:
        p=5.00
    elif c==2:
        p=6.50
    elif c==3:
        p=5.00
    return u, p*u

def dulce():
    c=0
    u=0
    p=0
    print("\n\tDelicias de dulce\n")
    print("1. Pastel...............$20.00")   
    print("2. Galletas..............$3.50")
    print("3. Pai de limon..............$30.00")
    c=int(input("por favor, seleccione una opcion: "))
    u=int(input("cuantas unidades desea?: "))
    if c==1:
        p=20.00
    elif c==2:
        p=3.50
    elif c==3:
        p=30.00
    return u, p*u

def main():
    opc=0
    total=0
    unidades=0
    while opc!=5:
        opc=menu()
        if opc==1:
            u, t = calientes()
            unidades = unidades + u
            total = total + t
        elif opc==2:
            u, t = frios()
            unidades = unidades + u
            total = total + t
        elif opc==3:
            u, t = sal()
            unidades = unidades + u
            total = total + t
        elif opc==4:
            u, t = dulce()
            unidades = unidades + u
            total = total + t
        elif opc<=0 or opc>5:
            print("opcion no valida")
    print(f"total a pagar: ${total} y unidades: {unidades}")

main()
