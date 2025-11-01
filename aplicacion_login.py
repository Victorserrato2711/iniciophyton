import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Creamos ventana
ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('icono.ico')

#Configuramos etiquetas y Cuadro de texto
entrada_usuario = ttk.Entry(ventana,width=30)
entrada_usuario.grid(row=0, column=1, columnspan=2,pady=5, padx=5)
entrada_password = ttk.Entry(ventana,width=30, show='*')
entrada_password.grid(row=1, column=1, columnspan=2,pady=5, padx=5)

#Generamos etiquetas
etiqueta_usuario = tk.Label(ventana, text='Usuario',fg='blue')
etiqueta_usuario.grid(row=0, column=0, pady=5, padx=5)
etiqueta_contraseña = tk.Label(ventana, text='Contraseña', fg='blue')
etiqueta_contraseña.grid(row=1, column=0, pady=5, padx=5)

def login():
    mensaje1 = entrada_usuario.get()
    mensaje2 = entrada_password.get()
    messagebox.showinfo('Mensaje Informativo', f'Usuario: {mensaje1}, Contraseña:{mensaje2}'  )

#Creamos boton
boton_login = ttk.Button(ventana, text='Login', command=login)
boton_login.grid(row=3, column=1, pady=10)

ventana.mainloop()