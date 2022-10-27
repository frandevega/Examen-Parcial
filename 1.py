class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(" el alumno ha sido creado con éxito")
    def clasificacion(self,nota):
        if nota<5:
            return ("el alumno ha suspendido")
        else:
            return("el alumno ha aprobado")

a=alumno("Antonio",8)
b=alumno("Juan",10)
c=alumno("Jesus",2)
lista=[a,b,c]
for i in lista:
    print (i.clasificacion(i.nota))



