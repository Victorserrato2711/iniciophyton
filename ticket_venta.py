print('*** Generación Ticket de Venta ***')
precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio Pan: '))
precio_lechuga = float(input('Precio Lechuga: '))
precio_platano = float(input('Precio Platano: '))
descuento_porcentaje = int(input('Aplicar algun descuento(%)? '))
# Calculo del Subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano
# Aplicar Descuento
descuento = subtotal * (descuento_porcentaje/100)
# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento
# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16
#Calculo de total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuestos (16%): ${impuesto:.2f}
Costo Total de la compra ${costo_total_compra:.2f}''')