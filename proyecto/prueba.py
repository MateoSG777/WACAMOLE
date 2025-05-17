##Martin Andres Obregoso - Mateo Sanchez Garcia 05/05/2025
## Este programa permite gestionar el registro y vacunación de mascotas.
def saludar():
    print("\n\nBienvenido al sistema de vacunación de mascotas \n")
    print("Este programa permite gestionar el registro y vacunación de tus mascotas.\n")
    print("Por favor registre los datos de administrador")
    input("Presione ENTER para continuar...")

def menu_principal():
    print("\n\t\t\t SISTEMA DE VACUNACIÓN")
    print("\nPor favor, seleccione una opción:")
    print("\n1. Acceso Administrador")
    print("2. Acceso Beneficiario")      
    print("3. Registro de Mascotas")
    print("\n4. Salir")
    a = input("Seleccione opción: ")
    return a

def setup_inicial():
    saludar()
    print("\n=== CONFIGURACIÓN INICIAL ===")
    admin_pin = input("Establezca PIN del Administrador: ")
    tipo_vacuna = input("Tipo de vacuna a administrar: ")
    total_dosis = int(input("Cantidad total de dosis disponibles: "))
    return [admin_pin, tipo_vacuna, total_dosis, total_dosis] # último valor son dosis disponibles y el otro es para el resumen en el administrador 

def registrar_mascota_interesadas(config, beneficiarios):
    if config[3] < 4:
        print("\nNo hay dosis suficientes disponibles")
        return

    print("\n=== REGISTRO DE MASCOTA ===")
    propietario = input("Nombre del propietario: ")
    cedula = input("Número de identificación: ")
    nombre_mascota = input("Nombre de la mascota: ")
    tipo_mascota = ""
    while tipo_mascota not in ["Perro", "Gato"]:
        tipo_mascota = input("Tipo de mascota (Perro/Gato): ").capitalize()
    edad = int(input("Edad de la mascota: "))

    nuevo = [propietario, cedula, nombre_mascota, tipo_mascota, edad, 4, [0, 0, 0, 0]] ## el valor 6 es una sublista con el estado de las dosis 
    beneficiarios.append(nuevo)
    config[3] -= 4 ## dependiendo del numero de dosis totales que ingrese el administrador se le restan 4 ya que cada mascota puede tener 4 dosis 
    print(f"\nAprobado, se han asignado 4 dosis para {nombre_mascota}")

def mostrar_beneficiarios(beneficiarios):
    print("\nLista de Beneficiarios:")
    for b in beneficiarios: ## b seria una sublista con los datos de cada beneficiario 
        dosis_recibidas = 0
        for dosis in b[6]: ## recorre la sublista en la poscision 6 que es el estado de las dosis 
            dosis_recibidas += dosis ## suma las dosis que ya esten dadas 
        print(f"Propietario: {b[0]}, Mascota: {b[2]} ({b[3]}), Dosis recibidas: {dosis_recibidas}/4")

def solicitar_dosis(beneficiario):
    for i in range(4):
        if beneficiario[6][i] == 0: ## contiene estado de las dosis que no han sido dadas = 0
            beneficiario[6][i] = 1  ## contiene estado de las dosis que han sido dadas = 1
            print(f"\nDosis {i+1} administrada") ## i va a ser el numero de dosis que han sido administradas como 1 o 3 dosis administradas  
            return
    print("\nYa fueron recibidas todas las dosis")

def mostrar_dosis(beneficiario):
    print("\nEstado de dosis:")
    for i in range(4):
        estado = "Administrada"
        if beneficiario[6][i] != 1:  # Si no está administrada
            estado = "Pendiente"
        print(f"Dosis {i+1}: {estado}")

def menu_beneficiario(config, beneficiarios):
    print("\n=== ACCESO BENEFICIARIO ===")
    print("1. Ingresar como beneficiario")
    print("2. Registrarse como nuevo beneficiario")
    print("3. Volver")

    opcion = input("Seleccione opción: ")
    if opcion == "1":
        acceso_beneficiario(beneficiarios)
    elif opcion == "2":
        registrar_mascota_interesadas(config, beneficiarios)
    elif opcion == "3":
        return
    else:
        print("\nOpción invalida")

def acceso_beneficiario(beneficiarios):
    cedula = input("\nIngrese numero de identificación: ")
    for beneficiario in beneficiarios:
        if beneficiario[1] == cedula: ## verifica el codigo de acceso al beneficiario en este caso la cedula 
            opcion = "0"
            while opcion != "4":
                print(f"\nBienvenido {beneficiario[0]}")
                print(f"Mascota: {beneficiario[2]} ({beneficiario[3]})")
                print("1. Ver estado de vacunación")
                print("2. Solicitar siguiente dosis")
                print("3. Ver historial de dosis")
                print("4. Volver")

                opcion = input("Seleccione opción: ")
                if opcion == "1":
                    dosis_recibidas = 0  ## se inicia en 0 para ver las dosis dadas indivudualmente a cada beneficiario 
                    for dosis in beneficiario[6]: ## recorre la sublista de dosis que esta en la posicion 6 y por cada dosis dada va a recorrer la lista 
                        dosis_recibidas += dosis ## suma cada dosis para ponerlas en la variable y contar el total 
                    print(f"\nDosis recibidas: {dosis_recibidas}/4")
                elif opcion == "2":
                    solicitar_dosis(beneficiario)
                elif opcion == "3":
                    mostrar_dosis(beneficiario)
            return
    print("Beneficiario no encontrado")

def mostrar_estadisticas(config, beneficiarios):
    print("\n=== ESTADISTICAS GENERALES ===")
    total_mascotas = 0
    for _ in beneficiarios:  ## el _ sirve para porque no necesitamos el valor de del elemento beneficiarios 
        total_mascotas += 1  ## cada vez que lo recorre y hay un beneficiario se suma en el contador 

    total_dosis_otorgadas = 0
    for b in beneficiarios:
        for dosis in b[6]: ## recorre la lista beneficiarios y el contador b representa cada beneficiario individualmente 
            total_dosis_otorgadas += dosis ## cada beneficiario tiene la sublista en el indice 6 que significaria la cantidad de dosis administradas y en esta lista esta 0 = si no ha sido administrada y 1 = si ya fue administrada y por cada 1 que haya en esta lista se va sumando para dar las estadisticas 
                                           
    print(f"Total de mascotas registradas: {total_mascotas}")
    print(f"Total de dosis administradas: {total_dosis_otorgadas}")
    print(f"Dosis disponibles: {config[3]}")

def menu_admin(config, beneficiarios):
    pin = input("\nIngrese PIN del administrador: ")
    if pin != config[0]:  ## config es una lista que contiene el pin del administrador y aca valida si es incorrecta 
        print("PIN incorrecto")
        return  ## este return vacio sirve para que le de fin a la funcion menu_admin despues de verificarla 

    opcion = "0"
    while opcion != "4":
        print("\n=== MENU ADMINISTRADOR ===")
        print("1. Ver lista de beneficiarios")
        print("2. Ver estadisticas")
        print("3. Ver mascotas por tipo")
        print("4. Volver")

        opcion = input("Seleccione opción: ")
        if opcion == "1":
            mostrar_beneficiarios(beneficiarios)
        elif opcion == "2":
            mostrar_estadisticas(config, beneficiarios)
        elif opcion == "3":
            mostrar_mascotas_por_tipo(beneficiarios)

def mostrar_mascotas_por_tipo(beneficiarios):
    perros = 0
    gatos = 0
    total = len(beneficiarios)
    
    for b in beneficiarios:
        if b[3] == "Perro":
            perros += 1 
        elif b[3] == "Gato":
            gatos += 1
            
    print(f"\nPerros registrados: {perros}")
    print(f"Gatos registrados: {gatos}")
    
    # Cálculo de porcentajes solo si hay mascotas registradas
    if total > 0:
        porcentaje_perros = (perros * 100) / total
        porcentaje_gatos = (gatos * 100) / total
        print(f"Porcentaje perros: {porcentaje_perros}%")
        print(f"Porcentaje gatos: {porcentaje_gatos}%")
        
        # Mostrar población mayoritaria
        if perros > gatos:
            print("La población con mayor beneficio son los Perros")
        elif gatos > perros:
            print("La población con mayor beneficio son los Gatos")
        else:
            print("Ambas poblaciones tienen igual cantidad de beneficiarios")

def consultar_interes():
    a = ""
    while a != "si" and a != "no":
        print("\n=== REGISTRO DE INTERES ===")
        a = input("¿Desea registrarse para recibir el beneficio? (Si/No): ").lower()
        if a != "si" and a != "no":
            print("\nPor favor responda Si o No")
    return a

def main():
    beneficiarios = []
    config = setup_inicial()
    opcion = "0"

    while opcion != "4":
        opcion = menu_principal()
        if opcion == "1":
            menu_admin(config, beneficiarios)
        elif opcion == "2":
            menu_beneficiario(config, beneficiarios)
        elif opcion == "3":
            if consultar_interes() == "si":
                registrar_mascota_interesadas(config, beneficiarios)
            else:
                print("\nGracias por su interes. Volviendo al menu principal...")
        elif opcion != "4":
            print("\nOpcion invalida")
            print("Por favor seleccione una opcion valida")
    print("\nPrograma finalizado")

main()