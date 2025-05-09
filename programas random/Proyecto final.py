def menu_principal():
    print("\n\n\n\n\n\nBienvenido al sistema de beneficios de la comunidad vulnerable TDAH")
    print("\n\t\t\t SISTEMA DE BENEFICIOS")
    print("\nPor favor, seleccione una opción:")
    print("\n1. Acceso Administrador")
    print("2. Acceso Beneficiario") 
    print("3. Registro de Interesados")
    print("\n4. Salir")
    return input("Seleccione opción: ")

def setup_inicial():
    print("\n=== CONFIGURACIÓN INICIAL ===")
    admin_pin = input("Establezca PIN administrativo: ")
    tipo_beneficio = input("Tipo de beneficio a otorgar: ")
    valor_total = float(input("Valor total disponible: "))
    max_beneficiarios = int(input("Cantidad máxima de beneficiarios: "))
    return [admin_pin, tipo_beneficio, valor_total, max_beneficiarios]

def registrar_interesado(config, beneficiarios, interesados):
    if len(beneficiarios) >= config[3]:
        print("\nNo hay cupos disponibles")
        return

    print("\n=== REGISTRO DE INTERESADO ===")
    nombre = input("Nombre completo: ")
    cedula = input("Número de cédula: ")
    edad = int(input("Edad: "))
    print("\nTipos de población:")
    print("1. Estudiante")
    print("2. Trabajador")
    print("3. Adulto mayor")
    poblacion = input("Seleccione tipo de población: ")
    puntaje_tdah = float(input("Puntaje TDAH (1-5): "))

    # Lista temporal con datos del interesado
    nuevo = [nombre, cedula, edad, poblacion, puntaje_tdah]

    # Validar elegibilidad
    if edad >= 6 and puntaje_tdah >= 3:
        beneficio = config[2] / config[3]
        nuevo.append(beneficio)
        nuevo.append([0, 0, 0, 0])  # Control de entregas
        beneficiarios.append(nuevo)
        print(f"\n¡Aprobado! Beneficio asignado: ${beneficio:,.2f}")
    else:
        interesados.append(nuevo)
        print("\nNo cumple requisitos mínimos")

def menu_beneficiario(beneficiarios):
    cedula = input("\nIngrese número de cédula: ")
    for beneficiario in beneficiarios:
        if beneficiario[1] == cedula:
            opcion = "0"
            while opcion != "4":
                print(f"\nBienvenido {beneficiario[0]}")
                print("1. Ver beneficio asignado")
                print("2. Solicitar entrega")
                print("3. Ver entregas realizadas")
                print("4. Volver")
                
                opcion = input("Seleccione opción: ")
                if opcion == "1":
                    print(f"\nBeneficio total: ${beneficiario[5]:,.2f}")
                    print(f"Valor por entrega: ${beneficiario[5]/4:,.2f}")
                elif opcion == "2":
                    solicitar_entrega(beneficiario)
                elif opcion == "3":
                    mostrar_entregas(beneficiario)
            return
    print("Beneficiario no encontrado")

def menu_admin(config, beneficiarios, interesados):
    pin = input("\nIngrese PIN administrativo: ")
    if pin != config[0]:
        print("PIN incorrecto")
        return

    opcion = "0"
    while opcion != "5":
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Ver lista de interesados")
        print("2. Ver lista de beneficiarios")
        print("3. Ver estadísticas")
        print("4. Ver promedio TDAH")  # New option
        print("5. Volver")
        
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            mostrar_interesados(interesados)
        elif opcion == "2":
            mostrar_beneficiarios(beneficiarios)
        elif opcion == "3":
            mostrar_estadisticas(config, beneficiarios)
        elif opcion == "4":
            calcular_promedio_tdah(beneficiarios)  # New function call

def mostrar_interesados(interesados):
    print("\nLista de Interesados:")
    for i in interesados:
        print(f"Nombre: {i[0]}, Cédula: {i[1]}")

def mostrar_beneficiarios(beneficiarios):
    print("\nLista de Beneficiarios:")
    for b in beneficiarios:
        print(f"Nombre: {b[0]}, Beneficio: ${b[5]:,.2f}")

def solicitar_entrega(beneficiario):
    for i in range(4):
        if beneficiario[6][i] == 0:
            beneficiario[6][i] = 1
            print(f"\nEntrega {i+1} realizada")
            return
    print("\nYa recibió todas las entregas")

def mostrar_entregas(beneficiario):
    print("\nEstado de entregas:")
    for i in range(4):
        estado = "Entregado" if beneficiario[6][i] == 1 else "Pendiente"
        print(f"Entrega {i+1}: {estado}")

def mostrar_estadisticas(config, beneficiarios):
    print("\n=== ESTADÍSTICAS GENERALES ===")
    print(f"Total beneficiarios: {len(beneficiarios)}")
    total_entregado = sum(b[5] for b in beneficiarios)
    print(f"Total beneficios asignados: ${total_entregado:,.2f}")
    print(f"Disponible: ${config[2] - total_entregado:,.2f}")

def calcular_promedio_tdah(beneficiarios):
    """
    Calcula y muestra el promedio de puntaje TDAH de beneficiarios
    """
    if not beneficiarios:
        print("\nNo hay beneficiarios registrados")
        return
        
    total_puntaje = sum(b[4] for b in beneficiarios)
    promedio = total_puntaje / len(beneficiarios)
    print(f"\nPromedio de puntaje TDAH: {promedio:.2f}")

def main():
    beneficiarios = []
    interesados = []
    config = setup_inicial()
    opcion = "0"
    while opcion != "4":
        opcion = menu_principal()
        if opcion == "1":
            menu_admin(config, beneficiarios, interesados)
        elif opcion == "2":
            menu_beneficiario(beneficiarios)
        elif opcion == "3":
            registrar_interesado(config, beneficiarios, interesados)
        elif opcion == "4":
            print("\nPrograma finalizado")
        else:
            print("\nOpción inválida")
main()