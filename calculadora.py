print(f'*** Calculadora con funciones ***')

def captura_valores():
    valor_1 = float(input(f'Ingresa el valor 1: '))
    valor_2 = float(input(f'Ingresa el Valor 2: '))
    return valor_1,valor_2

if __name__ == '__main__':

    while True:
        print('Opciones Disponibles')
        print(''' \t1. Sumar
    2. Restar
    3. Multiplicacion
    4. Division.
    5. Salir.''')

        opcion = int(input('Selecciona una opcion: '))

        if opcion == 1:
            valor_1, valor_2 = captura_valores()
            resultado = valor_1 + valor_2
            print(f'El Resultado de la operacion es: {resultado}')

        elif opcion == 2:
            valor_1, valor_2 = captura_valores()
            resultado = valor_1 - valor_2
            print(f'El Resultado de la operacion es: {resultado}')

        elif opcion == 3:
            valor_1, valor_2 = captura_valores()
            resultado = valor_1 * valor_2
            print(f'El Resultado de la operacion es: {resultado}')

        elif opcion == 4:
            valor_1, valor_2 = captura_valores()
            resultado = valor_1 / valor_2
            print(f'El Resultado de la operacion es: {resultado}')

        elif opcion == 5:
            print('Saliendo de la Calculadora, hasta luego')
            break
        else:
            print(f'Opcion Invalida Intenta de Nuevo')
