myStr = "Hello World"

print(dir(myStr))
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Hola')) #PARA REEMPLAZAR PALABRAS
print(myStr.count('l')) #SOLO CUENTA EL CARACTER
print(myStr.startswith('He')) #BUSCA SI EL TEXTOS INICIA CON LA PALABRA QUE HEMOS PUESTO EN LAS COMILLAS, 
                              #SI COINCIDE EL TEXTO, DARA TRUE, SI NO, TIRARA FALSE
print(myStr.endswith('rld')) #BUSCA SI EL TEXTOS TERMINA CON LA PALABRA QUE HEMOS PUESTO EN LAS COMILLAS, 
                             #SI COINCIDE EL TEXTO, DARA TRUE, SI NO, TIRARA FALSE

print(myStr.split()) #SEPARA A PARTIR DE UN CARACTER EN BLANCO
print(myStr.split(',')) #SEPARA A PARTIR DE UNA COMA