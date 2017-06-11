import xml.sax
import xml.etree.ElementTree as ET

class Usuario(object):
    def __init__(self,nombre=None,contra=None):
        self.nombre = nombre
        self.contra = contra
    
class NodoCircular(object):
    def __init__(self,matriz=None,cola=None,siguiente=None,usuario=None,anterior=None):
        self.matriz = matriz
        self.cola = cola
        self.siguiente = self
        self.anterior = self
        self.usuario = usuario
 
class ListaCircular(object):
    def __init__(self,acceso=None):
        self.acceso = acceso
    def insertar(self,dato):
        nuevo = NodoCircular()
        if self.acceso is not None:
            nuevo.usuario = dato
            nuevo.anterior = self.acceso
            nuevo.siguiente = self.acceso.siguiente
            self.acceso.siguiente.anterior = nuevo
            self.acceso.siguiente = nuevo
        else:
            nuevo.usuario = dato
            nuevo.anterior = nuevo
            nuevo.siguiente = nuevo
            self.acceso = nuevo
    def buscar(self,dato):
        actual = self.acceso
        if (actual.usuario.nombre == dato.nombre) and (actual.usuario.contra == dato.contra):
             return True
        actual = actual.siguiente
        while actual != self.acceso:
            if (actual.usuario.nombre == dato.nombre) and (actual.usuario.contra == dato.contra):
                return True
            actual = actual.siguiente
        return False
    
class Nodo(object):

    def __init__(self, dato=None,siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
		
class Pila(object):
    
    def __init__(self, top=None):
        self.top=top
    
    def vacia(self):
        if self.top is None:
            return True
        else:
            return False
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.top
        self.top = nuevo;
    def pop(self):
        a = self.top.dato
        self.top = self.top.siguiente;
        return a
    def top(self):
        return top.dato;
    def limpiar(self):
        while(not vacia()):
            pop()
        return "pila vaciada"

class cola(object):
    def __init__(self, inicio=None, fin=None):
        self.inicio = inicio
        self.fin = fin
    
    def vacia(self):
        if self.inicio is None:
            return True
        else:
            return False
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if(self.vacia()):
            self.inicio = nuevo
        else:
            self.fin.siguiente = nuevo
        self.fin = nuevo
    def extraer(self):
        a = self.inicio.dato
        self.inicio = self.inicio.siguiente
        return a
    def inicio(self):
        return self.inicio.dato
    def fin():
        return self.fin.dato
    def limpiar():
        while(not self.vacia()):
    	     extraer()

class Lista(object):

    def __init__(self,cabeza=None):
        self.cabeza = cabeza

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.get_siguiente()
        return count

    def buscar(self,dato):
        contador = 0
        actual = self.cabeza
        encontrado = False
        while actual and encontrado is False:
            if actual.get_dato() == dato:
                encontrado = True
                "valor encontrado en" + str(contador)
            else:
                actual = actual.get_siguiente()
        i+=1
        if actual is None:
            raise ValueError("Dato no encontrado")
        return "valor no encontrado"
    
    def buscarin(self,indice):
        encontrado = False
        actual = self.cabeza
        for i in range(0,indicie):
            if actual.siguiente is not None:
                actual = actual.siguiente
            else:
                return 'Dato no encontrado'
        return actual.dato
    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        encontrado = False
        while actual is not None and encontrado is False:
            if actual.get_dato() == dato:
                encontrado = True
            else:
                previo = actual
                actual = actual.get_siguiente()
        if actual is not None:
            if(actual==self.cabeza):
                self.cabeza = actual.siguiente
            else:
                previo.siguiente = actual.siguiente
            actual = None
            return "valor eliminado"
        else:
             return "valor no encontrado"

class Matriz(object):  
    def __init__(self,x,y):
        indice = Lista()
        for i in range(0,x):
            indice.insertar(Lista())
            for j in range(0,y):
                indice.
            print (i)

mat = Matriz(5,5)

usuarios = ListaCircular()
u = Usuario("asf","fdsa")

usuarios.insertar(Usuario("prueba","fdasio"))
usuarios.insertar(u)

def graficarusuarios():
    actual = usuarios.acceso
    a= actual.usuario.nombre + " -> "
    while actual.siguiente != usuarios.acceso:
        actual = actual.siguiente
        a = a  + actual.usuario.nombre + " -> "   
    a = a  + actual.siguiente.usuario.nombre
    print(a)
    
def graficarusuarios2():
    actual = usuarios.acceso
    a= actual.usuario.nombre + " -> "
    while actual.anterior != usuarios.acceso:
        actual = actual.anterior
        a = a  + actual.usuario.nombre + " -> "
    a = a  + actual.anterior.usuario.nombre
    print(a)

def crear():
    nombre = input("Ingrese el nombre: " )
    contra = input("Ingrese la contraseña: ")
    usu = Usuario(nombre,contra)
    usuarios.insertar(usu)
    print('Usuario creado')
    print()
    menuprincipal()
    
def menuprincipal():
    print("Ingrese una opcion: ","1. Crear Usuario","2. Ingresar al sistema", "3. Salir del programa", sep="\n")
    opcion = input()
    if opcion == "1":
        crear()
    elif opcion == '2':
        ingresar()

def opciones():
    print("1. Leer archivo", "2. Resolver operaciones", "3. Operar la matriz", "4. Mostrar usuarios", "5. Mostrar cola", "6. Cerrar sesion",sep="\n")
    opcion = input()
    if opcion == '1':
        leer()
        
def leer():
    archivo = input("Ingrese el nombre del archivo: ")
    tree = ET.parse(archivo)
    root = tree.getroot()
    
    for matriz in root.findall('matriz'):
        x = matriz.find('x').text
        y = matriz.find('y').text
        print (x,y)
    
    for operacion in root.iter('operacion'):
        print(operacion.text)

    
def operaciones():
    print("1. Operar siguiente", "2. Regresar", sep="\n")

def menumatriz():
    print("1. Ingresar Dato","2. Operar Transpuesta", "3. Mostrar Matriz Original", "4. Mostrar Matriz Transpuesta", "5. Regresar", sep="\n")

def ingresar():
    nombre = input("Ingrese el nombre: ")
    contra = input("Ingrese la contraseña: ")
    if usuarios.buscar(Usuario(nombre,contra)):
        print('Bienvenido')
        opciones()

menuprincipal()

