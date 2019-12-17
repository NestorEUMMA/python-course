myStr = "Hello World"
name = "Nestor Ulloa"

#print(dir(myStr))
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())
print(myStr.replace('Hello', 'Hola')) #PARA REEMPLAZAR PALABRAS
print(myStr.count('l')) #SOLO CUENTA EL CARACTER
print(myStr.startswith('He')) #BUSCA SI EL TEXTOS INICIA CON LA PALABRA QUE HEMOS PUESTO EN LAS COMILLAS, 
                              #SI COINCIDE EL TEXTO, DARA TRUE, SI NO, TIRARA FALSE
print(myStr.endswith('rld')) #BUSCA SI EL TEXTOS TERMINA CON LA PALABRA QUE HEMOS PUESTO EN LAS COMILLAS, 
                             #SI COINCIDE EL TEXTO, DARA TRUE, SI NO, TIRARA FALSE

print(myStr.split()) #SEPARA A PARTIR DE UN CARACTER EN BLANCO
print(myStr.split(',')) #SEPARA A PARTIR DE UNA COMA
print(myStr.find('o')) #BUSCA LA LETRA O CARACTER PERO BUSCA LA POSICION BASADA EN UN NUMERO, EN EL EJEMPLO LA LETRA "O" ESTA EN LA POSICION 4
print(len(myStr)) #CUENTA LA CANTIDAD DE CARACTERES COMENZANDO POR EL NUMERO 0
print(myStr.index('e')) #MUESTRA EL INDICE DE LA LETRA, EN EL EJEMPLO LA VOCAL "e" ESTA EN LA SEGUNDA POSICION, CONTANDO DESDE 0, SERIA EL INDEX 1
print(myStr.isnumeric()) #VALIDA SI EL STRING ES NUMERICO
print(myStr.isalpha()) #VALIDA SI EL STRING ES ALFANUMERICO
print(myStr[4]) #MUESTRA UNICAMENTE LA LETRA/VOCAL QUE ESTA EN ESA POSICION

print("Mi nombre es: " + name) #PODEMOS CONCATENAR UN OBJETO