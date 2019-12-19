demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']
#r = list(range(1,10)) #MUESTRA UNA LISTA CON RANGOS

#print(len(demo_list)) #MUESTRA LA CANTIDAD DE PALABRAS QUE TENGO EN LA LISTA, EN EL EJEMPLO REGRESARA 5
#print(colors[2]) #MUESTRA EL INDICE DE LOS ELEMENTOS, EN EL EJEMPLO ME REGRESARA BLUE
#print('green' in colors) #DEVOLVERA UN TRUE O FALSE SI SE ENCUENTRA EL ELEMENTO EN LA LISTA
#print(demo_list)
#print(r)

#********** SE PUEDE AGREGAR UN INPUT Y METERLO EN EL INDEX QUE SE LE DEFINA
#print(colors)
#colors[1] = input("Ingrese un color: ")
#colors.append(input("Ingrese un color: ")) #SE PUEDE AGREGAR UN NUEVO ELEMENTO A LA LISTA, YA SEA POR UN INPUT O POR UN ELEMENTO ESTATICO.
#colors.extend(['violet', 'yellow', 'brown']) #SE PUEDE AGREGAR UN NUEVO ELEMENTO A LA LISTA, YA SEA POR UN INPUT O POR UN ELEMENTO ESTATICO.
colors.insert(1, 'brown') #INSERTA UN ELEMENTO EN EL INDEX INDICADO
colors.pop() #QUITA UN ELEMENTO DE LA LISTA
colors.remove('green') #QUITA EL ELEMENTO QUE INGRESAMOS DE UNA LISTA
colors.clear() #DEJA VACIA LA LISTA
print(colors)