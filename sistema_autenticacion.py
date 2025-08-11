print(f'*** Sistema de Validacion ***')

usuario_txt = 'vserrato'
contraseña = 'phyton2025'
mensaje_bienvenida = None

#Solicitamos Usuario y Contraseña
usuario_cap = input(f'Ingresa tu Usuario: ')
contraseña_cap = input(f'Ingresa tu contraseña: ')
usuario = usuario_cap.strip().lower()

#Validaciones
if usuario == usuario_txt and contraseña_cap == contraseña:
    mensaje_bienvenida = 'Bienvenido al sistema'
elif usuario != usuario_txt and contraseña_cap == contraseña:
    mensaje_bienvenida = 'Usuario Incorrecto'
elif usuario == usuario_txt and contraseña_cap != contraseña:
    mensaje_bienvenida = 'Contraseña Incorrecta'
else:
    mensaje_bienvenida = 'Usuario y Contraseña Incorrecta'

print(f'{mensaje_bienvenida}')