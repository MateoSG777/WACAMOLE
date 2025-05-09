def saludar():
    print("\n\n\n\n\n\nBienvenido al sistema de vacunación de mascotas \n")
    print("Este programa permite gestionar el registro y vacunación de mascotas.\n")
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
    return (a)

def setup_inicial():
    saludar()
    print("\n=== CONFIGURACIÓN INICIAL ===")
    admin_pin = input("Establezca PIN administrativo: ")
    tipo_vacuna = input("Tipo de vacuna a administrar: ")
    total_dosis = int(input("Cantidad total de dosis disponibles: "))
    return [admin_pin, tipo_vacuna, total_dosis, total_dosis] # último valor son dosis disponibles

def registrar_mascota_interesadas(config, beneficiarios, interesados):
    if config[3] < 4:  # Verificar si hay suficientes dosis
        print("\nNo hay dosis suficientes disponibles")
        return

    print("\n=== REGISTRO DE MASCOTA ===")
    propietario = input("Nombre del propietario: ")
    cedula = input("Número de identificación: ")
    nombre_mascota = input("Nombre de la mascota: ")
    tipo_mascota = ""
    while tipo_mascota not in ['Perro', 'Gato']:
        tipo_mascota = input("Tipo de mascota (Perro/Gato): ").capitalize()
    edad = int(input("Edad de la mascota: "))

    nuevo = [propietario, cedula, nombre_mascota, tipo_mascota, edad, 4, [0, 0, 0, 0]]
    beneficiarios.append(nuevo)
    config[3] -= 4  # Actualizar dosis disponibles
    print(f"\n¡Aprobado! Se han asignado 4 dosis para {nombre_mascota}")

def mostrar_beneficiarios(beneficiarios):
    print("\nLista de Beneficiarios:")
    for b in beneficiarios:
        dosis_recibidas = sum(b[6])
        print(f"Propietario: {b[0]}, Mascota: {b[2]} ({b[3]}), Dosis recibidas: {dosis_recibidas}/4")

def solicitar_dosis(beneficiario):
    for i in range(4):
        if beneficiario[6][i] == 0:
            beneficiario[6][i] = 1
            print(f"\nDosis {i+1} administrada")
            return
    print("\nYa recibió todas las dosis")

def mostrar_dosis(beneficiario):
    print("\nEstado de dosis:")
    for i in range(4):
        estado = "Administrada" if beneficiario[6][i] == 1 else "Pendiente"
        print(f"Dosis {i+1}: {estado}")

def menu_beneficiario(config, beneficiarios, interesados):
    print("\n=== ACCESO BENEFICIARIO ===")
    print("1. Ingresar como beneficiario")
    print("2. Registrarse como nuevo beneficiario")
    print("3. Volver")
    
    opcion = input("Seleccione opción: ")
    if opcion == "1":
        acceso_beneficiario(beneficiarios)
    elif opcion == "2":
        registrar_mascota_interesadas(config, beneficiarios, interesados)  # Error: config and interesados not defined
    elif opcion == "3":
        return
    else:
        print("\nOpción inválida")

def acceso_beneficiario(beneficiarios):
    cedula = input("\nIngrese número de identificación: ")
    for beneficiario in beneficiarios:
        if beneficiario[1] == cedula:
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
                    dosis_recibidas = sum(beneficiario[6])
                    print(f"\nDosis recibidas: {dosis_recibidas}/4")
                elif opcion == "2":
                    solicitar_dosis(beneficiario)
                elif opcion == "3":
                    mostrar_dosis(beneficiario)
            return
    print("Beneficiario no encontrado")

def mostrar_estadisticas(config, beneficiarios):
    print("\n=== ESTADÍSTICAS GENERALES ===")
    total_mascotas = len(beneficiarios)
    total_dosis_otorgadas = sum(sum(b[6]) for b in beneficiarios)
    print(f"Total de mascotas registradas: {total_mascotas}")
    print(f"Total de dosis administradas: {total_dosis_otorgadas}")
    print(f"Dosis disponibles: {config[3]}")

def menu_admin(config, beneficiarios):
    pin = input("\nIngrese PIN administrativo: ")
    if pin != config[0]:
        print("PIN incorrecto")
        return

    opcion = "0"
    while opcion != "4":
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Ver lista de beneficiarios")
        print("2. Ver estadísticas")
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
    perros = sum(1 for b in beneficiarios if b[3] == "Perro")
    gatos = sum(1 for b in beneficiarios if b[3] == "Gato")
    print(f"\nPerros registrados: {perros}")
    print(f"Gatos registrados: {gatos}")

def consultar_interes():
    while True:
        print("\n=== REGISTRO DE INTERÉS ===")
        interes = input("¿Desea registrarse para recibir el beneficio? (Si/No): ").lower()
        if interes in ["si", "no"]:
            return interes == "si"
        print("\nPor favor responda Si o No")

def main():
    beneficiarios = []
    interesados = []
    config = setup_inicial()
    opcion = "0"

    while opcion != "4":
        opcion = menu_principal()
        if opcion == "1":
            menu_admin(config, beneficiarios)
        elif opcion == "2":
            menu_beneficiario(config, beneficiarios, interesados)
        elif opcion == "3":
            if consultar_interes():
                registrar_mascota_interesadas(config, beneficiarios, interesados)
            else:
                print("\nGracias por su interés. Volviendo al menú principal...")
        elif opcion != "4":
            print("\nOpción inválida")
            print("Por favor, seleccione una opción válida")
    print("\nPrograma finalizado")
main()