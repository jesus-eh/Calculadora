def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Resta', accion1),
        '2': ('Suma', accion2),
        '3': ('Division', accion3),
        '4': ('Multiplicacion', accion4),
        '5': ('Conversor a fahrenheit', accion5),
        '6': ('Coneversor de euro - dolar', accion6),
        '7': ('Conversor de euro-pesos mexicanos', accion7)
    }

    generar_menu(opciones, '10')


def accion1():
    a = int(input("Introduzca un numero : "))
    b = int(input("Introduzca otro numero : "))
    resta = a - b
    print("la resta es : ", resta )

def accion2():
    a = int(input("Introduzca un numero : "))
    b = int(input("Introduzca otro numero : "))
    suma = a + b
    print("La suma es : ", suma)


def accion3():
    a = int(input("Introduzca un numero : "))
    b = int(input("Introduzca otro numero : "))
    division = a / b
    print("La Division es : ", division)


def accion4():
    a = int(input("Introduzca un numero : "))
    b = int(input("Introduzca otro numero : "))
    multiplicacion = a * b
    print("La Multiplicacion es : ", multiplicacion)


def accion5():
    c = int(input("Escribe los grados que quieres psasa fahrenheit :"))
    conversor = 9 / 5 * c + 32
    print("Son ", conversor, "fahrenheit")


def accion6():
    euro = int(input("introduzca el cambio : "))
    conversion = euro * 1.07
    print("Tienes ", conversion, "$")


def accion7():
    euro2 = int(input("Introduzca el cambio : "))
    conversion2 = euro2 * 20.27
    print("Tienes ", conversion2, "MXN")


if __name__ == '__main__':
    menu_principal()

#By Jesus Escaño herrero
