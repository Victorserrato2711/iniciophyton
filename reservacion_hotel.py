print(f'*** Reservacion Hotel ***')

#Variables Fijas
costos_vista_mar = 190.50 #por Dia
costo_sin_vista = 150.50 #por dia

#Datos solicitados al Cliente
nombre_cliente = str(input(f'Cual es su nombre?: '))
dias_estadia = int(input(f'Cuantos dias seria su hospedaje?: '))
cuarto_con_vista = input('Desea Cuarto con vista al mar (Si/No)?: ')
cuarto_con_vista = cuarto_con_vista.strip().lower()

#Costos
total_vista = dias_estadia * costos_vista_mar
total_sin_vista = dias_estadia * costo_sin_vista

#Validacion de datos
if not cuarto_con_vista == 'si':
    print(f'''\n ------------- Detalles de la Reservacion -------------)
    Hola {nombre_cliente}
    Selecciono una cuarto sin vista al mar por un total de 
    {dias_estadia} dias 
    El Monto total Seria de ${total_sin_vista:.2f}''')

else:
    print(f''' \n ------------- Detalles de la Reservacion -------------)
    Hola {nombre_cliente}
    Selecciono una cuarto Con vista al mar por un total de 
    {dias_estadia} dias 

    El Monto total Seria de ${total_vista:.2f}''')
