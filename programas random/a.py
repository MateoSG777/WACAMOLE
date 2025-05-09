def main():
    s1 = 50
    s2 = 90
    s3 = 120
    a = 20.000
    b = 15.000
    c = 12.000
    total = 0
    pal = 20.000

    print("Bienvenido a la venta de boletos de cine")
    print("la boleta de la sala 1 tiene un precio de $20.000")
    print("la boleta de la sala 2 tiene un precio de $15.000")
    print("La boleta de la sala 3 tiene un precio de $12.000")
    print("El combo de crispetas y gaseosa es de $20.000")
    ans = input("le gustaría comprar boletas? si/no: ")

    while ans == "si":
        ans1 = int(input("¿en cual sala le gustaría estar? 1,2 o 3: "))
        if ans1 == 1:
            ans2 = int(input("Cuantas boletas le gustaría comprar?: "))
            if ans2 <= s1:
                ans3 = int(input("cuantos combos te crispetas y gaseaosas le gustaría comprar?: "))
                s1 = s1 - ans2
                subtotal = ans2 * a + ans3 * pal
                frequent = input("¿Es usted un cliente frecuente? si/no: ")
                if frequent == "si":
                    subtotal = subtotal * 0.9  # Apply 10% discount
                total = total + subtotal
            else:
                print("No hay más boletos para esta sala.")
        elif ans1 == 2:
            ans2 = int(input("Cuantas boletas le gustaría comprar?: "))
            if ans2 <= s2:
                ans3 = int(input("cuantos combos te crispetas y gaseaosas le gustaría comprar?: "))
                s2 = s2 - ans2
                subtotal = ans2 * b + ans3 * pal
                frequent = input("¿Es usted un cliente frecuente? si/no: ")
                if frequent == "si":
                    subtotal = subtotal * 0.9  # Apply 10% discount
                total = total + subtotal
            else:
                print("No hay más boletos para esta sala.")
        elif ans1 == 3:
            ans2 = int(input("Cuantas boletas le gustaría comprar?: "))
            if ans2 <= s3:
                ans3 = int(input("cuantos combos te crispetas y gaseaosas le gustaría comprar?: "))
                s3 = s3 - ans2
                subtotal = ans2 * c + ans3 * pal
                frequent = input("¿Es usted un cliente frecuente? si/no: ")
                if frequent == "si":
                    subtotal = subtotal * 0.9  # Apply 10% discount
                total = total + subtotal
            else:
                print("No hay más boletos para esta sala.")
        ans = input("le gustaría comprar más boletas? si/no: ")

    print("Ventas terminadas. Las ventas del día de hoy fueron:")
    print("sala1: cantidad de boletos vendidos: ", 50 - s1)
    print("sala2: cantidad de boletos vendidos: ", 90 - s2)
    print("sala3: cantidad de boletos vendidos: ", 120 - s3)
    print("cantidad de combos vendidos es: ", pal)
    print("total de ventas $", total)
    print("Fin")

main()