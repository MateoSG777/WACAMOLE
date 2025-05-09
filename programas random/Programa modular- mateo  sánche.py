def precios_y_cantidad_de_boletos_por_salas():
    return 50, 90, 120, 20.000, 15.000, 0,  12.000, 20.000

def print_bienvenida():
    print("Bienvenido a la venta de boletos de cine")
    print("la boleta de la sala 1 tiene un precio de $20.000")
    print("la boleta de la sala 2 tiene un precio de $15.000")
    print("La boleta de la sala 3 tiene un precio de $12.000")
    print("El combo de crispetas y gaseosa es de $20.000")

def proceso_de_compra(voletos, combos, precio, pal, total):
    subtotal = voletos * precio + combos * pal
    total = total + subtotal
    return total

def comprar_boletos(sala, boletos_disponibles, precio, pal, total):
    ans2 = int(input("Cuantas boletas le gustaría comprar?: "))
    if ans2 <= boletos_disponibles:
        ans3 = int(input("cuantos combos te crispetas y gaseaosas le gustaría comprar?: "))
        boletos_disponibles = boletos_disponibles - ans2
        total = proceso_de_compra(ans2, ans3, precio, pal, total)
    else:
        print(f"Hay esta cantidad de boletos restantes en la sala {sala}: {boletos_disponibles}, por lo que no se pueden comprar más boletos.")
    return boletos_disponibles, total

def aplicar_descuento(total):
    frequent = str(input("¿Es usted un cliente frecuente? si/no: "))
    if frequent == "si":
        total = total * 0.9  # Apply 10% discount
    return total

def print_ventas(s1, s2, s3, pal, total):
    print("Ventas terminadas. Las ventas del día de hoy fueron:")
    print("sala1: cantidad de boletos vendidos: ", 50 - s1)
    print("sala2: cantidad de boletos vendidos: ", 90 - s2)
    print("sala3: cantidad de boletos vendidos: ", 120 - s3)
    print("cantidad de combos vendidos es: ", pal)
    print("total de ventas $", total)
    print("Fin del programa")

def main():
    s1, s2, s3, a, b, c, total, pal = precios_y_cantidad_de_boletos_por_salas()
    print_bienvenida()
    ans = input("le gustaría comprar boletas? si/no: ")

    while ans == "si":
        ans1 = int(input("¿en cual sala le gustaría estar? 1,2 o 3: "))
        if ans1 == 1:
            s1, total = comprar_boletos(1, s1, a, pal, total)
        elif ans1 == 2:
            s2, total = comprar_boletos(2, s2, b, pal, total)
        elif ans1 == 3:
            s3, total = comprar_boletos(3, s3, c, pal, total)
        ans = input("le gustaría comprar más boletas? si/no: ")

    total = aplicar_descuento(total)
    print_ventas(s1, s2, s3, pal, total)

main()