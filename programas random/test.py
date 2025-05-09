def convertidor():
    print("convertidor de temperatura")
    print("1. Celsius a Fahrenheit")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def celsius_mostar():
    x = int(input("Ingrese la temperatura en grados Celsius: "))
    print(f"La temperatura en grados Farennheit es: {celsius_a_fahrenheit(x)}")

def convertido_2():
    print("Convertidor de temperatura")
    print("2. Fahrenheit a Celsius")

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def farenheit_mostrar():
    x = int (input("Ingrese la temperatura en grados Fahrenheit: "))
    print(f"La temperatura en grados Celcius es : {fahrenheit_a_celsius(x)*40}")
def despedida():
    print("Gracias por usar el convertidor de temperatura")
def main():
    convertidor()
    celsius_mostar()
    convertido_2()
    farenheit_mostrar()
    despedida()
main()
