import xml.sax
import xml.etree.ElementTree as ET
from sys import exit
class Usuario(object):
    def __init__(self,nombre=None,contra=None,matriz=None):
        self.nombre = nombre
        self.contra = contra
        self.cola = cola()
        self.matriz = matriz
        self.cargado = False
class NodoCircular(object):
    def __init__(self,siguiente=None,usuario=None,anterior=None):
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
             return actual.usuario
        actual = actual.siguiente
        while actual != self.acceso:
            if (actual.usuario.nombre == dato.nombre) and (actual.usuario.contra == dato.contra):
                return actual.usuario
            actual = actual.siguiente
        return None
    def buscaru(self,dato):
        actual = self.acceso
        if (actual.usuario.nombre == dato.nombre) and (actual.usuario.contra == dato.contra):
             return True
        actual = actual.siguiente
        while actual != self.acceso:
            if (actual.usuario.nombre == dato.nombre) and (actual.usuario.contra == dato.contra):
                return actual.usuario
            actual = actual.siguiente
        return None
    
class Nodo(object):

    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
		
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
        while actual.siguiente is not None:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def modificar(self,indice,dato ):
        encontrado = False
        actual = self.cabeza
        for i in range(0,indice):
            if actual.siguiente is not None:
                actual = actual.siguiente
        actual.dato = dato
    
    def buscarin(self,indice ):
        encontrado = False
        actual = self.cabeza
        for i in range(0,indice):
            if actual.siguiente is not None:
                actual = actual.siguiente
            else:
                return None
        return actual.dato

class Matriz(object):  
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.indice = Lista()
        for i in range(0,y):
            nueva = Lista()
            for j in range(0,x):
                
                nueva.insertar(0)
            self.indice.insertar(nueva)
            #print(self.indice.buscarin(i).tamanio())
            
    def graficarmat(self):
        a = ''
        for i in range(0,self.y):
            for j in range(0,self.x):
                a = a + " " + str(self.indice.buscarin(i).buscarin(j))
            print('|' + a + '|')
            a = ''
            
    def insertar(self,x,y,dato):
        if(x < self.x and y < self.y):
            self.indice.buscarin(x).modificar(y,dato)
            print('El dato ha sido ingresado')
        else:
            print("los valores son incorrectos")
        
    def graficartrans(self):
        a = ''
        for i in range(0,self.x):
            for j in range(0,self.y):
                a = a + " " + str(self.indice.buscarin(j).buscarin(i))
            print('|' + a + '|')
            a = ''

mat = Matriz(5,5)

usuarios = ListaCircular()
u = Usuario("asf","fdsa")

usuarios.insertar(Usuario("prueba","fdasio"))
usuarios.insertar(u)
#print(mat.indice.tamanio())

#print(mat.indice.buscarin(2).buscarin(3))
#mat.insertar(2,2,5)
#mat.graficarmat()
nombre = ''
contra = ''
usuarioactivo = Usuario()

stack = Pila()

def ingresar():
    nombre = input("Ingrese el nombre: ")
    contra = input("Ingrese la contraseña: ")
    if usuarios.buscar(Usuario(nombre,contra)) is not None:
        global usuarioactivo
        usuarioactivo = usuarios.buscar(Usuario(nombre,contra))
        print('Bienvenido')
        opciones()
    else:
        print('Ingreso invalido')
        print('')
        menuprincipal()

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
    elif opcion == '3':
        exit()
    else:
        print(' ')
        menuprincipal()

def opciones():
    print("1. Leer archivo", "2. Resolver operaciones", "3. Operar la matriz", "4. Mostrar usuarios", "5. Mostrar cola", "6. Cerrar sesion",sep="\n")
    opcion = input()
    global usuarioactivo
    if opcion == '1':
        leer()   
    elif opcion == '2' and usuarioactivo.cargado:
        operaciones()
    elif opcion == '3' and usuarioactivo.cargado:
        menumatriz()
    elif opcion == '4':
        graficarusuarios()
        print('')
        graficarusuarios2()
        print('')
        opciones()
    elif opcion == '5':
        graficarcola()
        opciones()
    elif opcion == '6': 
        usuarioactivo = None
        menuprincipal()
    else:
        print(' ')
        opciones()
        

def leer():
    archivo = input("Ingrese el nombre del archivo: ")
    tree = ET.parse(archivo)
    root = tree.getroot()
    global usuarioactivo
    if not usuarioactivo.cargado:
        for matriz in root.findall('matriz'):
            x = matriz.find('x').text
            y = matriz.find('y').text
            usuarioactivo.matriz = Matriz(int(x),int(y))
    else:
        print('Matriz Existente')
    for operacion in root.iter('operacion'):
        usuarioactivo.cola.insertar(operacion.text)
    print('archivo leido')
    usuarioactivo.cargado = True
    print('')
    opciones()
    
def graficarcola():
    i = 0
    actual = usuarioactivo.cola.inicio
    if (usuarioactivo.cola.vacia()==True):
        pass
    else:
        while(actual != None):          
            if(actual.siguiente is not None):
                temp = Nodo()
                temp = actual.siguiente                
            print(actual.dato)
            actual = actual.siguiente
    
def operaciones():
    print("1. Operar siguiente", "2. Regresar", sep="\n")
    opcion = input()
    if opcion == '1':
        operar()
    elif opcion == '2':
        opciones()
    else:
        print('')
        operaciones()
def menumatriz():
    print("1. Ingresar Dato","2. Operar Transpuesta", "3. Mostrar Matriz Original", "4. Mostrar Matriz Transpuesta", "5. Regresar", sep="\n")
    opcion = input()
    global usuarioactivo
    if opcion == '1':
        x = input('Ingrese la posicion en X: ')
        y = input('Ingrese la posicion en Y: ')
        dato = input('Ingrese el dato: ')
        usuarioactivo.matriz.insertar(int(y),int(x),dato)
        
        print('')
        menumatriz()
    elif opcion == '2':
        transpuesta = usuarioactivo.matriz
        print('La matriz ha sido creada')
        menumatriz()
    elif opcion == '3':
        print('')
        usuarioactivo.matriz.graficarmat()
        print('')
        menumatriz()
    elif opcion == '4':
        usuarioactivo.matriz.graficartrans()
        print('')
        menumatriz()
    elif opcion == '5':
        opciones()
    else:
        print('')
        menumatriz()
def operar():
    ope = usuarioactivo.cola.extraer()
    lis = ope.split()
    lis.reverse()
    for p in lis:
        stack.push(p)
    while(not stack.vacia()):
        a = stack.pop()
        if stack.vacia():
            print('Resultado: ' + str(a))
            print('')
            break
        b = stack.pop()
        op = stack.pop()
        if op == '+':
            res = int(a) + int(b)
        elif op == '-':
            res = int(a) - int(b)
        elif op == '*':
            res = int(a) * int(b)
        stack.push(res)
        print(str(a) +  " " + str(op) + " " + str(b) + " = " + str(res))
    opciones()


menuprincipal()

