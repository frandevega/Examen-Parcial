class Nodo():
    '''Clase nodo simplemente enlazado'''
    
    def __init__(self, dato=None):
        self.dato = dato
        #Enlace al siguiente nodo. Por defecto el nodo no esta enlazado.
        self.sig = None

class Monomio():
    '''Clase monomio'''
    
    def __init__(self, coeficiente, exponente):
        ''''Crea un monomio con un coeficiente,a,  y exponente, b: ax^b '''
        self.coef = coeficiente
        self.expo = exponente
        
    def __str__(self):
        return '{}x^{}'.format(self.coef, self.expo)

        
class Polinomio():
        '''Dato abstracto de dato polinomio
        
        Se basa en una lista enlazada de monomios
        '''
        
        def __init__(self):
            #Grado del polinomio
            self.grado = -1
            self.cabeza = None
            
        def agregar_monomio(self, monomio):
            '''Agrega un monomio al polinomio'''
            
            nodo = Nodo(monomio)
            
            #El monomio pasa a la cabeza del polinomio
            if monomio.expo > self.grado:
                nodo.sig = self.cabeza
                self.cabeza = nodo
                self.grado = monomio.expo 
            else:
                #Recorremos el poliniomio en busca de su posicion correcta
                nodo_aux = self.cabeza

                while((nodo_aux.sig is not None) and (nodo_aux.sig.dato.expo > monomio.expo)):
                    nodo_aux = nodo_aux.sig
                
                #Insertamos el nodo en la posicion correcta: o en medio o al final
                
                #Comprobamos si el monino ya existe: si existe sumamos los coeficientes
                if (nodo_aux.dato.expo == monomio.expo):
                    nodo_aux.dato.coef += monomio.coef
                else:
                    nodo.sig = nodo_aux.sig
                    nodo_aux.sig = nodo

        def __str__(self):
        
            nodo_aux = self.cabeza
            
            #El primer monomio
            str_polinomio = '{}x^{}'.format(nodo_aux.dato.coef, nodo_aux.dato.expo)

            #Iteramos sobre el resto de nodos
            nodo_aux = nodo_aux.sig

            while (nodo_aux is not None):
                str_polinomio += ' + {}x^{}'.format(nodo_aux.dato.coef, nodo_aux.dato.expo)
                #Avanzamos el nodo
                nodo_aux = nodo_aux.sig
        
            return str_polinomio
        
        def modificar_monomio(self, monomio):
            '''Reemplaza un monomio en el polinomio'''
            
            nodo_aux = self.cabeza

            while (nodo_aux is not None):
                if nodo_aux.dato.expo == monomio.expo:
                    break
                
                #Avanzamos el nodo
                nodo_aux = nodo_aux.sig
            
            nodo_aux.dato.coef = monomio.coef
            
        def elmininar_termino(self, exponente):
            '''Elimina el coeficiente para el monomio de exponente de entrada'''
            pass

        def restar_polinomio(self,polinomio):
            paux = Polinomio()
            poli1 = self.cabeza

            while (poli1 is not None):
                
                poli2 = polinomio.cabeza
                
                while (poli2 is not None):
                    
                    nuevo_expo = poli1.dato.expo - poli2.dato.expo
                    coef = paux.obtener_coeficiente(nuevo_expo)
                    paux.agregar_monomio(Monomio(nuevo_expo))

                    poli2 = poli2.sig
                 
                poli1 = poli1.sig
            
            return paux
                   
        def dividir_polinomio(self, valor):   
            '''Multiplica el polinomio por el valor de entrada'''
            pass 
        
        def multiplica_polinomio(self, polinomio):   
            '''Multiplicamos por el polinomio de entrada'''
            
            paux = Polinomio()
            poli1 = self.cabeza

            while (poli1 is not None):
                
                poli2 = polinomio.cabeza
                
                while (poli2 is not None):
                    
                    nuevo_expo = poli1.dato.expo + poli2.dato.expo
                    nuevo_coef = poli1.dato.coef + poli2.dato.coef
                    coef = paux.obtener_coeficiente(nuevo_expo)
                    
                    if(coef is not None):
                        nuevo_coef += coef
                        paux.modificar_monomio(Monomio(nuevo_coef, nuevo_expo))
                    else:
                        paux.agregar_monomio(Monomio(nuevo_coef, nuevo_expo))

                    poli2 = poli2.sig
                 
                poli1 = poli1.sig
            
            return paux
                       
                       
                       
##############################################                     
                                   
polinomio = Polinomio()

#Anadimos un termino
mono = Monomio(1, 0)      

polinomio.agregar_monomio(mono)   

#Imprimimos el polinomio
print(polinomio)

#Anadimos otro termino
polinomio.agregar_monomio(Monomio(3, 2))
   
#Imprimimos el polinomio
print(polinomio)

#Anadimos otro termino
polinomio.agregar_monomio(Monomio(2, 1)) 

#Imprimimos el polinomio
print(polinomio)

#Anadimos otro termino
polinomio.agregar_monomio(Monomio(4, 3)) 

#Imprimimos el polinomio
print(polinomio)

#Anadimos otro termino
polinomio.agregar_monomio(Monomio(90, 3)) 

#Imprimimos el polinomio
print(polinomio)
 
 
#Anadimos otro termino
polinomio.modificar_monomio(Monomio(7, 3)) 

#Imprimimos el polinomio
print(polinomio)

print("Coeficiente: {}".format(polinomio.obtener_coeficiente(2)))

#Sumamos un polinomio: el que ya tenemos
polinomio2 = copy.deepcopy(polinomio)
polinomio.suma_polinomio(polinomio2)

#Imprimimos el polinomio
print(polinomio)
            
#Sumamos un polinomio: el que ya tenemos
polinomio2 = copy.deepcopy(polinomio)

polinomio2.agregar_monomio(Monomio(9, 4)) 

polinomio.suma_polinomio(polinomio2)

#Imprimimos el polinomio
print(polinomio)


print(polinomio.multiplica_polinomio(polinomio2))
