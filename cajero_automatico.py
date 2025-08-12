print(f'*** Aplicacion de Cajero Automatico ***')

DEPOSITADO = 1000
salir = False
deposito = None
retiro = None

while not salir:
    print(f'''Operaciones que puede realizar
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input(f'Seleccione una opcion: '))
    if opcion == 1:
        print(f'Tu Saldo es ${DEPOSITADO}\n')
    elif opcion == 2:
        retiro = float(input(f'\nIngrese la Cantidad a Retirar: '))
        if retiro <=0:
            print('La Cantidad debe ser mayor a Cero.\n')
        elif retiro > DEPOSITADO:
            print(f'Fondos insuficientes. Tu saldo es ${DEPOSITADO:.2f}\n')
        else:
            DEPOSITADO -= retiro
            print(f'Retiro exitoso. Tu saldo actual es de ${DEPOSITADO:.2F}\n' )
    elif opcion == 3:
        deposito = int(input(f'Ingresa la Cantidad a depositar: '))
        DEPOSITADO += deposito
        print(f'Tu Saldo actual es: ${DEPOSITADO:.2f}\n')
    elif opcion == 4:
        print(f'Gracias Por utilizar nuestro Cajero')
        salir = True
    else:
        print(f'Opcion Invalida. Favor de seleccionar otra opcion')
else:
    print(f'Saliendo del Cajero. Hasta pronto....')

