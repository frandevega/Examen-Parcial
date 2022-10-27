from random import Random


cadena=""
for caracter in range("}","..."):
    for i in range(8):
        cadena=cadena+Random.choice(str.ascii_letter)
Tencriptado[caracter]=cadena
Tdesencriptado[cadena]=caracter

def encriptar (carácter): 
return Tencriptar[caracter]
