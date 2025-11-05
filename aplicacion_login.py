import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        #Creamos ventana
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)

        self._crear_componentes()
        # Definir el metodo Crear componentes
    def _crear_componentes(self):
        #Configuramos Cuadro de texto
        self.entrada_usuario = ttk.Entry(self,width=30)
        self.entrada_usuario.grid(row=0, column=1, columnspan=2,pady=5, padx=5)
        self.entrada_password = ttk.Entry(self,width=30, show='*')
        self.entrada_password.grid(row=1, column=1, columnspan=2,pady=5, padx=5)

        #Generamos etiquetas
        etiqueta_usuario = tk.Label(self, text='Usuario',fg='blue')
        etiqueta_usuario.grid(row=0, column=0, pady=5, padx=5)
        etiqueta_contraseña = tk.Label(self, text='Contraseña', fg='blue')
        etiqueta_contraseña.grid(row=1, column=0, pady=5, padx=5)

        boton_login = ttk.Button(self, text='Login', command= self._login)
        boton_login.grid(row=3, column=1, pady=10)
    #Creamos boton
    def _login(self):
        mensaje1 = self.entrada_usuario.get()
        mensaje2 = self.entrada_password.get()
        messagebox.showinfo('Datos Loggin', f'Usuario: {mensaje1}, Contraseña: {mensaje2}'  )


#Ejecucion
if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()
