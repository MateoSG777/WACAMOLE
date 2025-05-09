def reglas():
    print("\n=== REGLAS DEL JUEGO ===")
    print("1. Salta sobre otras fichas")
    print("2. Mueve solo horizontal o vertical")
    print("3. Deja una sola ficha al final")
    input("\nPresiona Enter para volver...")

def jugar():
    nombre = input("\nTu nombre: ")
    print(f"\n¡Bienvenido {nombre}!")

    tablero = [
        [" ", " ", "O", "O", "O", " ", " "],
        [" ", " ", "O", "O", "O", " ", " "],
        ["O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "-", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O"],
        [" ", " ", "O", "O", "O", " ", " "],
        [" ", " ", "O", "O", "O", " ", " "]
    ]
    
    print("\nTablero inicial:")
    for fila in tablero:
        print(" ".join(fila))
    
    input("\nPresiona Enter para volver...")

def historia():
    print("\n=== HISTORIA DEL JUEGO ===")
    print("""El Peg Solitaire (también conocido como Hi-Q) es un juego de mesa para un solo jugador con origen incierto
, aunque se cree que apareció en la corte de Luis XIV en Francia a finales del siglo XVII. Su primera mención
documentada fue en 1697 en una ilustración de la revista francesa Mercure Galant.
El juego se popularizó en Europa y América con diferentes nombres y variaciones en el diseño del tablero
, siendo el más común el de forma de cruz o el de 33 agujeros con una disposición similar a la de una cruz griega.
En el siglo XX, compañías como Parker Brothers lo comercializaron bajo el nombre Hi-Q, aumentando su difusión.""")
    input("\nPresiona Enter para volver...")

def score():
    print("\n=== PUNTUACIÓN ===")
    print("La funcionalidad de puntuación estará disponible pronto.")
    input("\nPresiona Enter para volver...")

def menu():
    while True:
        print("\n=== SOLITARIO ===")
        print("1. Jugar")
        print("2. Reglas")
        print("3. Historia")
        print("4. Score")
        print("5. Salir")
        
        opcion = input("\nElige (1-5): ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            reglas()
        elif opcion == "3":
            historia()
        elif opcion == "4":
            score()
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida")
            input("Presiona Enter...")

menu()