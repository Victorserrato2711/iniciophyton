import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from cliente import Cliente

from zona_fit_app.cliente_dao import ClienteDAO


class App(tk.Tk):
    color_ventana = '#1d2d44'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()

    def limpiar_campos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        self.caja_nombre.delete(0,tk.END)
        self.caja_apellido.delete(0,tk.END)
        self.caja_membresia.delete(0,tk.END)

    def eliminar_registro(self):
        if self.id_cliente is None:
            showerror(title='Error', message='Favor Seleccionar cliente')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado', message='Cliente Eliminado')
            self.limpiar_campos()
        self.recargar_datos()

    def validar_cliente(self):
        #validar campos
        if(self.caja_nombre.get() and self.caja_apellido.get() and self.caja_membresia.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion', message='El valor de membresia no es numerico')
                self.caja_membresia.delete(0,tk.END)
                self.caja_membresia.focus_set()
        else:
            showerror(title='Atencion', message='Debe de llenar todo el formulario')
            self.caja_nombre.focus_set()

    def validar_membresia(self):
        try:
            int(self.caja_membresia.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        #Recuperar los valores  de las cajas de texto
        nombre = self.caja_nombre.get()
        apellido = self.caja_apellido.get()
        membresia = self.caja_membresia.get()
        #Validacion Id Cliente
        if self.id_cliente is None:
            cliente = Cliente(nombre= nombre, apellido=apellido,membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar', message='Cliente Agregado...')

        else:
            cliente = Cliente(self.id_cliente,nombre= nombre, apellido=apellido,membresia=membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualiza', message='Cliente Actualizado...')

        #Volvemos a mostrar los datos y limpieza de formularios
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values'] #tupla de valores
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        self.limpiar_formulario()
        self.caja_nombre.insert(0,nombre)
        self.caja_apellido.insert(0,apellido),
        self.caja_membresia.insert(0,membresia)

    def recargar_datos(self):
        #Volver a cargar los datos de la caja
        self.mostrar_tabla()
        #limpiar formulario
        self.limpiar_campos()

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        #crear los botones
        boton_agregar = ttk.Button(self.frame_botones,text='Guardar',
                                   command=self.validar_cliente)
        boton_agregar.grid(row=0, column=0, padx=30)

        boton_eliminar = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_registro)
        boton_eliminar.grid(row=0, column=1, padx=30)

        boton_limpiar = ttk.Button(self.frame_botones,text='Limpiar',
                                   command=self.limpiar_campos)
        boton_limpiar.grid(row=0, column=2, padx=30)

        #Estilo de botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        #Publicar Frame
        self.frame_botones.grid(row=3, column=0, columnspan=2)

    def mostrar_tabla(self):
        # Creamos Frame
        self.frame_tabla = ttk.Frame(self)
        #definicio estilos
        self.estilos.configure('Treeview', background='black', foreground='white',
                               fieldbackground='black',rowheight=20)
        #definimos columnas
        columnas= ('Id', 'Nombre', 'Apellido','Membresia')
        #Objeto Tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')


        #mostramos el Frame de Tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

        #Agregamos cabeceros
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        #Definir columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W ,width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre, cliente.apellido,cliente.membresia))
        #Agregamos Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview())
        self.tabla.configure(yscroll = scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #Asocial al Evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # mostramos tabla
        self.tabla.grid(row=0, column=0)

    def mostrar_formulario(self):
        self.frame_formulario = ttk.Frame()
        #Creamos Etiquetas
        etiqueta_nombre = ttk.Label(self.frame_formulario, text='Nombre:')
        etiqueta_nombre.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        etiqueta_apellido= ttk.Label(self.frame_formulario, text='Apellido:')
        etiqueta_apellido.grid(row=1,column=0,sticky=tk.W, pady=30, padx=5)
        etiqueta_membresia = ttk.Label(self.frame_formulario, text='Membresía')
        etiqueta_membresia.grid(row=2,column=0,sticky=tk.W, pady=30, padx=5)


        #Creamos Cajas de Texto
        self.caja_nombre = ttk.Entry(self.frame_formulario)
        self.caja_nombre.grid(row=0, column=1, sticky=tk.E,)
        self.caja_apellido = ttk.Entry(self.frame_formulario)
        self.caja_apellido.grid(row=1, column=1, sticky=tk.E)
        self.caja_membresia = ttk.Entry(self.frame_formulario)
        self.caja_membresia.grid(row=2, column=1, sticky=tk.E)

        #publicacion frame
        self.frame_formulario.grid(row=1, column=0)

    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

    def mostrar_titulo(self):
        etiqueta_titulo = ttk.Label(self, text='Zona Fit(Gym)', font=('Arial', 15),
                                    background=App.color_ventana, foreground='white')
        etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=30)

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.color_ventana)
        #Aplicacion Estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') #Preparamos para modo oscuro
        self.estilos.configure(self, background=App.color_ventana,
                       foreground='white',
                       fieldbackground='black')




if __name__ == '__main__':
    app = App()
    app.mainloop()