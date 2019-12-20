#FORMA DE CREAR UNA FUNCION
def hello(name):
    print("Hello " + name)
hello("Nestor")
hello("Katita")
hello("Miranda")


#FORMA DE CREAR UNA FUNCION CON RETURN
def add(numberOne, numberTwo):
    return numberOne + numberTwo
print(add(10,30))


#ESTA ES OTRA FORMA DE CREAER UNA FUNCION
add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10,50))