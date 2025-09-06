def rest(num):
    return num - 1
def sum(num):
    return num + 1     #Defino funciones de operaciones basicas para usar en el codigo (Avance 2)
def sum2(num1, num2):
    return num1 + num2 
#Primer Algoritmo 
print("Visualiza las teclas WASD como flechas")
print("Escoje un movimiento, w:1 a:2 s:3 d:4 ")
movimientos = ["arriba", "izquierda", "abajo", "derecha"] #Se usa una lista para asignarle variables a los movimientos.
a = int(input()) #Le pide un número del 1 al 4 al usuario
movimiento = movimientos[ rest(a)] #Se usa la funcion de restar por que la lista empieza a valorar con 0, no en 1.
print(movimiento)               #Asi el numero dado por el usuario se resta con 1 y regresa el movimiento correcto de la lista. 
b = int(input())
movimiento = movimientos[ rest(b)] #Se repite lo anterior 3 veces mas para una muestra de rango de movimiento completo.
print(movimiento)
c = int(input())
movimiento = movimientos[ rest(c)]
print(movimiento)
d = int(input())
movimiento = movimientos[ rest(d)]
print(movimiento)
#Segundo Algoritmo                 #Interpreto mi segundo algoritmo con variables y funciones basicas
print("Ganaste una bolita? Si: 1 No:0?")
gb = int(input())                   #Pregunto al usuario si gano o no bolita con numeros
print("Tu tamaño es de: ", sum(gb) )      #Como el tamaño base es 1, uso la funcion de sumar 1 para mostrar el nuevo tamaño
print("Ganaste una bolita? Si: 1 No:0?")
gb2 = int(input())                        #Se repite 
print("Tu tamaño es de: ", sum2(sum(gb),gb2)) #Uso una funcion de sumar dos numeros para sumar el tamaño anterior con el nuevo
#Tercer Algoritmo                             #Interpreto mi tercer algoritmo con if, else
print("Chocaste con alguna pared? Si:1 No:0") 
sn = int(input())                             
if sn == 1:
    print("mueres")                      
else:
    print("vives")
    


