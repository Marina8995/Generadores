#Utilidad yield from: Simplificar el código de los generadores en el caso de utilizar bucles anidados

#Ejemplo 1

def devuelve_ciudades(*ciudades):

    #Estamos definiendo una función a través de una tupla. El * delante del argumento indica que no
    #  sabemos el número de argumentos que son. Esos argumentos los va a recibir en forma de tupla

    for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")      
#Aqui estamos accediendo a los elementos

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Ejemplo 2
#Para acceder a los subelementos, mediante bucle for anidado:

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")  

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Ejemplo 3
#Forma simplicifada de acceder a los subelementos sin el bucle for. Utilizando yield from:

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")  

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))