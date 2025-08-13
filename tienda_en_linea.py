print(f'*** Sistema descuentos en linea***')
#Condiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input(f'Cuanto es el monto de la Compra?: '))
es_miembro = str(input(f'Eres Miembro de la Tienda (Si/No)? '))

descuento = 0

#Verificacion de caso
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == 'si':
    descuento = 0.1 #Descuento del 10%

elif es_miembro.strip().lower() == 'si':
    descuento = 0.05 #Descuento del 5%

elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = .03 #Descuento del 3%

else:
    descuento = 0

# Hacemos los los calculos respectivos para obtener el monto final
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra: {monto_compra:.2f}')
    print(f'Monto del descuento: {monto_descuento:.2f}')
    print(f'Monto final de la compracon descuento: ${monto_final:.2f}')
else:
    print(f'\nNo obtuviste ningun tipo de descuento')
    print(f'Te invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: {monto_compra:.2f}')


