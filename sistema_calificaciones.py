print(f'*** Sistema Calificaciones ***')

calificacion_num = float(input(f'Proporciona la Calificacion numerica (0-10): '))
calificaion_letra = None
#Revision de los rangos
if calificacion_num >= 9 and calificacion_num <= 10:
    calificaion_letra = 'A'
elif calificacion_num >= 8 and calificacion_num <= 9:
    calificaion_letra = 'B'
elif calificacion_num >= 7 and calificacion_num <= 8:
    calificaion_letra = 'C'
elif calificacion_num >= 6 and calificacion_num <= 7:
    calificaion_letra = 'D'
elif calificacion_num >= 0 and calificacion_num <= 6:
    calificaion_letra = 'F'
else:
    calificaion_letra = 'Calificacion Incorrecta'
#Imprimir
print(f'Calificacion {calificacion_num} es equivalente a {calificaion_letra}')