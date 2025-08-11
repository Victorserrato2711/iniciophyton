print(f'**** Cotizador Sistema de Envios ****')
print('Para Cotizar tu envio favor de Capturar la siguiente informacion:')

#Costos por kilo
costo_nac = 10
costo_int = 20

dest_txt = (input(f'Ingreso el destino del paquete (nacional/internacional): '))
peso = float(input(f'Captura el peso del paquete: '))
costo_total = None
destino = dest_txt.strip().lower()

if destino == 'internacional':
    costo_total = peso * costo_int
elif destino == 'nacional':
    costo_total = peso * costo_nac
else:
   print(f'Error al Capturar Datos')

#impresion de valores
if costo_total is not None:
    print(f'El costo del envio del paquete es: ${costo_total:.2f}')