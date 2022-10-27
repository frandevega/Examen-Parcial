class producto:
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print ("el producto ha sido creado con exito")
    def __str__(self):
        return"(codigo: {}, nombre: {},precio: {}, tipo {})".format(self.codigo,self.nombre,self.precio,self.tipo)

a=producto(2.1,"chocolate",5,"comida")
b=producto(2.2,"azucar",2,"comida")
c=producto(11,"escoba",2,"limpieza")
print(a)
a.precio=8
print(a)
