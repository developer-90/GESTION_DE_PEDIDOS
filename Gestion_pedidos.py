#A nuestro equipo de desarrollo de software nos ha llegado la petición de un cliente para el diseño y
#desarrollo de una aplicación de gestión de pedidos.

#El cliente necesita una aplicación en donde un posible cliente se registre en la aplicación para realizar un
#pedido de los productos que están disponibles en la tienda online.

#Los clientes pueden ser nacionales o de fuera de España. Esto conlleva un reto añadido, puesto que el
#cálculo de sus pedidos se deberán ajustar a la legislación vigente en cada territorio.

#La aplicación estará desarrollada en Python aunque el análisis previo se realiza en pseudocódigo y
#diagramas de flujo.

#Las principales operaciones que necesitaremos gestionar serán:
    #Registro de cliente. Se pedirán sus datos personales y de facturación.
    #Selección de productos. Se permitirá añadir productos a la lista de deseos.
    #Compra y pago de los productos solicitados. Se enviará al cliente la factura en PDF a su correo
    #electrónico.

#Seguimiento. Se enviará por SMS al teléfono móvil y al correo del cliente el código de seguimiento de su
#pedido.

#El desarrollo de la aplicación consta de varias fases:
#Fase 1.
#En este primer paso, se explicar en este ejemplo qué es un algoritmo y cómo podríamos proponer una
#solución. Es importante, definir los pasos necesarios para resolver cada uno de los ítems que el cliente
#nos ha pedido, así como diseñar el organigrama correspondiente. En este primer paso, no es necesario
##desarrollar la aplicación en ningún lenguaje de programación. Se trata en todo caso, de analizar la
#organización y métodos de resolución de la aplicación.

#Fase 2.
#A continuación, nos dedicamos a la implementación de la aplicación. En este punto, sí es necesario
#utilizar Python para su desarrollo diseñando las clases, atributos, métodos, constructores necesarios para
#la aplicación. Debemos tener presente que no se nos pide realizar el aplicativo visual, únicamente la
#funcionalidad de cada caso.

#Fase 3.
#Para finalizar, deberemos analizar qué paradigma de programación hemos utilizado y qué características
#estamos aplicando en cada solución. Deberemos evaluar la conveniencia o no de utilizar otros
#paradigmas diferentes para llevar a cabo la resolución de los ítems planteados.

import random
from tkinter.tix import Select

# imprimimos mensaje por pantalla con la funcion print, incluyendo saltos de linea con \n
print('\n**********************************')
print('   BIENVENIDO A NUESTRO SISTEMA')
print('**********************************')

# creamos la clase persona
class Persona:
 # definimos un metodo constructor para almacenar informacion   
    def __init__(self) -> None: 
        print('\n   ===> REGISTRO <===\n')
        self.nombre=str(input('Introduzca su nombre: '))
        self.nif=str(input('Introduzca su NIF: '))
        self.direccion=str(input('Introduzca su direccion: '))
        self.pais=str(input('Introduzca el pais: '))
        self.telefono=int(input('Introduzca su telefono: '))
        self.correo=str(input('Introduzca su correo: '))

# definimos un metodo infoPersona para mostrar la informacion almacenada
    def infoPersona(self):       
        print('\nLos datos introducidos son:')
        print(f'Nombre: {persona1.nombre} - NIF: {persona1.nif} - direccion: {persona1.direccion} - telefono: {persona1.telefono} - correo: {persona1.correo}')


persona1=Persona() # creamos el objeto persona1
persona1.infoPersona() # llamamos al metodo infoPersona para mostrar los datos almacenados

# creamos la clase Producto
class Producto:
# definimos un metodo constructor    
    def __init__(self,nombre,unidades,precio): 
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    
    def hacerPedido(self):
        lista=[p1,p2]
        for p in lista:
            print(f'\n{p.nombre.capitalize()}')
            print(f'{p.precio} €/unidad')
        selectproduct=input(f'\n¿Que producto desea?: ')
        
        while selectproduct.lower() != p1.nombre.lower() and selectproduct.lower() != p2.nombre.lower():
            print(f'Error. Intentelo de nuevo')
            selectproduct=input(f'\n¿Que producto desea?: ')
        
        selectunid=int(input('¿Cuantas unidades?: '))

        print(f'\nHa seleccionado {selectunid} unidades de {selectproduct.lower()}')
        totalPedido=float(p1.precio)*selectunid
        print(f'El total es {totalPedido.__round__(2)} euros.')

        if persona1.pais.lower() == 'españa':
            print('\n>>>>> 21% de IVA <<<<<')
            calculo=selectunid*float(p1.precio)
            calculoIVA=selectunid*float(p1.precio)*1,21
            print(f'Precio sin IVA {calculo.__round__(2)}\nPrecio con IVA {calculoIVA.__round__(2)}')
        else:
            numeroIVA = random.randint(1, 21)
            print(f'\n>>>>> {numeroIVA}% de IVA <<<<<')
            calculo=selectunid*float(p1.precio)
            calculoIVA=selectunid*float(p1.precio)*((numeroIVA/100)+1)
            print(f'Precio sin IVA {calculo.__round__(2)} euros.\nPrecio con IVA {calculoIVA.__round__(2)} euros.')


# definimos el metodo seguimiento y establecemos la funcion print para imprimir por pantalla dos mensajes
    def seguimiento(self):
        print(f'\nEnvio codigo seguimiento por SMS a {persona1.telefono}')
        print(f'\nEnvio codigo seguimiento por email a {persona1.correo}')    

# definimos un metodo monstrarPedido para mostrar los datos del pedido y definimos el metodo random.randint que devuelve un numero entero para mostrar el numero de factura
# se establecen algunos metodos como .lower .upper y .capitalize para mostrar los datos en minisculas, mayusculas y primera letra en mayuscula para dar formato a la factura
    def mostrarPedido(self):  
        numeroFactura = random.randint(1, 9999)
        print(f'\nNº factura: {numeroFactura}')
        print(f'Datos del cliente:\n{persona1.nombre.upper()}\n{persona1.nif.upper()}\nTelefono: {persona1.telefono}\nEmail: {persona1.correo.lower()}')
        print(f'Direccion de envio: {persona1.direccion.capitalize()}, {persona1.pais.capitalize()}')

p1=Producto('tomates',' ','2.95')
p2=Producto('lechuga',' ','1.5')
p1.hacerPedido()
p1.seguimiento()
p1.mostrarPedido()
        

# alta de productos
print('\n¡¡ Vuelve pronto !!\n')



# internalizacion => segun el pais se cobra diferente iva al cliente
# se inventa el valor del iva fuera de españa
# deseo1=Pedido(idcliente,idproducto,unidades,fechacompra) METER VARIOS PRODUCTOS
# 
# 
# NOTA: briefing : reunion inicial cliente - product owner
# product owner -> scrum master
# scrum master - team : aplicacion
# PARTE 1
# casos de uso : uses case (UML) -> lucidchart software
# pseudocodigo : pseint
# diagrama de flujo : (pasos pseudocodigo)
# 
# registrarse
# seleccionar productos (lista de deseos) - HERENCIA?
# pagar
# seguimiento
# 
# sprint review : ultima vista del cliente
# hacer aplicacion escalable -> clase padre, clase hija....
# 
# persistencia de datos: insert table cliente (no hacer)
# 
# 
# 
# #