import math
import random


def generar_coordenada(lim_x, lim_y):
    val_x = lim_x * (2 * random.random() - 1)
    val_y = lim_y * (2 * random.random() - 1)
    return val_x, val_y


def pertenece_elipse(x, y, a, b):
    return x * x / (a * a) + y * y / (b * b) <= 1


def pertenece_hiperbola(x, y, c, d):
    return x * x / (c * c) - y * y / (d * d) >= 1


def pedir_flotante(texto):
    while True:
        try:
            num = float(input(texto))
            if num > 0:
                return num
            print("  Error: El valor debe ser mayor a cero.")
        except ValueError:
            print("  Error: Ingrese un numero valido.")


def pedir_entero(texto):
    while True:
        try:
            num = int(input(texto))
            if num > 0:
                return num
            print("  Error: El valor debe ser un entero positivo.")
        except ValueError:
            print("  Error: Debe ingresar un numero entero.")


def ejecutar_simulacion():
    print("*** CALCULO DE AREA POR SIMULACION MONTECARLO ***")
    a = pedir_flotante("Ingrese el valor de a: ")
    b = pedir_flotante("Ingrese el valor de b: ")
    c = pedir_flotante("Ingrese el valor de c: ")
    d = pedir_flotante("Ingrese el valor de d: ")
    iteraciones = pedir_entero("Ingrese la cantidad de puntos aleatorios: ")

    cont_elipse = 0
    cont_interseccion = 0

    for _ in range(iteraciones):
        x, y = generar_coordenada(a, b)

        if pertenece_elipse(x, y, a, b):
            cont_elipse += 1

            if pertenece_hiperbola(x, y, c, d):
                cont_interseccion += 1

    area_total = math.pi * a * b

    print("\n>>> REPORTE DE RESULTADOS (Monte Carlo)<<<")
    print(f"Puntos evaluados en total          : {iteraciones}")
    print(f"Puntos capturados por la elipse    : {cont_elipse}")
    print(f"Puntos capturados por la hiperbola : {cont_interseccion}")
    print(f"Area calculada de la elipse        : {area_total:.4f}")

    if cont_elipse == 0:
        print("No se encontraron puntos en la elipse. Intente con mas iteraciones.")
        return

    ratio = cont_interseccion / cont_elipse
    area_final = area_total * ratio

    print(f"Proporcion de interseccion         : {ratio:.4f}")
    print(f"AREA APROXIMADA DE LA INTERSECCION : {area_final:.4f}")


if __name__ == "__main__":
    ejecutar_simulacion()