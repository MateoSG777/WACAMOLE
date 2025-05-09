def menu():
    print("\nBienvenido al registro de estudiantes")
    print("1. resgistrar estudiante")
    print("2. ver estudiantes")    
    print("3. Buscar el mayor estudiante")
    print("4. Exit")
    a = int(input("\tSeleccione una opción: "))
    return a

def regitrar_estudiante(nom,ed,ind):
    ind = 0
    m = "s"
    print("\nRegistro de estudiantes")
    while ind < 5 and m == "s":
        nom[ind] = input("Ingrese el nombre del estudiante: ")
        ed[ind] = int(input("Ingrese la edad del estudiante: "))
        m = input("¿Desea registrar otro estudiante? (s/n): ")
        ind += 1
    return nom,ed,ind

def ver_estudiantes(nom,ed,ind):
    i2 = 0
    print("\nLista de estudiantes registrados")
    print("Nombre\tEdad")
    print("---------------------")
    while i2 < ind:
        print(nom[i2],"\t",ed[i2])
        i2 += 1
    return nom,ed,ind
def mayor_estudiante(nom,ed,ind):
    i2=0
    may=0
    pos=0
    while i2 < ind:
        if ed[i2] > may:
            may = ed[i2]
            pos = i2
        i2 += 1
    print(f"\nEl estudiante mayor es {nom[pos]} con {ed[pos]} años")
    return nom,ed,ind

def main():
    res_m = 0
    nom=[str]*5
    ed=[int]*5
    ind=0
    while res_m != 4:
        res_m = menu()
        if res_m == 1:
            nom,ed,ind = regitrar_estudiante(nom,ed,ind)
        elif res_m == 2:
            ver_estudiantes(nom,ed,ind)
        elif res_m == 3:
            mayor_estudiante(nom,ed,ind)
        elif res_m == 4:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intente de nuevo.")
main()