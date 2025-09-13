def rest(num):
    return num - 1
def sum(num):
    return num + 1     #Defino funciones de operaciones basicas para usar en el codigo 
def sum2(num1, num2):
    return num1 + num2 
#Primer Algoritmo 
print("Visualiza las teclas WASD como flechas")
print("Escoje un movimiento, w, a, s, d. ")      #se cambian las listas por condicionales if para saber los movimientos Avance 4 
mov = str(input())                                                          
if mov == "w":
    print("arriba")
elif mov == "a":
    print("izquierda")
elif mov == "s":
    print("abajo")
elif mov == "d":
    print("derecha")
else:
    print("Eso no es un movimiento")
#Segundo Algoritmo
#Interpreto mi segundo algoritmo con con condicionales if Avance 4
print("Tu tamaño base es de 1")
print("Ganaste una bolita? Si: 1 No:0?")
gb = int(input()) #Pregunto al usuario si gano o no bolita con numeros
if gb == 1:
    print("Tu tamaño es de: ", sum(gb))
else:
    print("Tu tamaño es de: ", gb) 
print("Ganaste una bolita? Si: 1 No:0?")
gb2 = int(input())
if gb2 == 1:
    print("Tu tamaño es de: ", sum2(sum(gb),gb2)) #Uso una funcion de sumar dos numeros para sumar el tamaño anterior con el nuevo
else:
    print("Tu tamaño es de: ", sum2(gb,gb2))
#Tercer Algoritmo                             #Interpreto mi tercer algoritmo con if, else
print("Chocaste con alguna pared? Si:1 No:0") 
sn = int(input())                             
if sn == 1:
    print("mueres")                      
else:
    print("vives")