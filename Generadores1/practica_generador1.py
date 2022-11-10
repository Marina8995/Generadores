#Diferencia entre función y generador

#Función:

def generaPares(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))        

#Generador

def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

devuelvepares=generaPares(10)  

for i in devuelvepares:

    print(i)    

#Ejemplo utilidad generador vs función

def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

devuelvepares=generaPares(10)  

print(next(devuelvepares))

print("Aqui podría ir más código")

print(next(devuelvepares))

print("Aqui podría ir más código")