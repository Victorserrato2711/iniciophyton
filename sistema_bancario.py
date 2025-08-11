print('*** Bienvenidos al Sistema Bancario ***')

salir_sistema_txt = input('Deseas salir del sistema (Si/No)? ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print(f'Continuamos dentro del sistema')
else:
    print(f'Salimos del sistema')
