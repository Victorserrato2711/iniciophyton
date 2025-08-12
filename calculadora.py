print(f'*** Calculadora ***')

SALIR = False
valor_1 = None
valor_2 = None

while not SALIR:
    print(f'''Indica la operacion a realizar
    1. Suma
    2. Resta
    3. multiplicacion
    4. division
    5. salir''')
    operacion = int(input(f'Indica que tipo de operaciones quieres hacer: '))
    if operacion == 1:
        valor_1 = float(input(f'Ingresa el primer Valor: '))
        valor_2 = float(input(f'Ingresa el Segundo Valor: '))
        resultado = valor_1 + valor_2
        print(f'El resultado es: {resultado:.2f}\n')
    elif operacion == 2:
        valor_1 = float(input(f'Ingresa el primer valor: '))
        valor_2 = float(input(f'Ingresa el segundo valor: '))
        resultado = valor_1 - valor_2
        print(f'El resultado es: {resultado}\n')
    elif operacion == 3:
        valor_1 = float(input(f'Ingresa el primer valor: '))
        valor_2 = float(input(f'Ingresa el segundo valor: '))
        resultado = valor_1 * valor_2
        print(f'El resultado es: {resultado}\n')
    elif operacion == 4:
        valor_1 = float(input(f'Ingresa el primer valor: '))
        valor_2 = float(input(f'Ingresa el segundo valor: '))
        resultado = valor_1 / valor_2
        print(f'El Resultado es: {resultado}\n')
    elif operacion == 5:
        SALIR = True
        print(f'Saliendo de Calculadora...')
    else:
        print(f'Opcion Invalida. Favor de seleccionar la opcion correcta\n')
