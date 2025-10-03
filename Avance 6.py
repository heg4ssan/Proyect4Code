import random    #Avance 6 (Listas, Ciclos for)
 
limpositivo = 15
limnegativo = 0
nc = "no colisiona"
c = "colisiona"

ANCHO = 15
ALTO = 15

def movimientos():                   
    usuario = ""
    while usuario != "terminar":
        usuario = input()
        if usuario == "terminar":
            break
        else:
            if usuario == "w":
                print("arriba")
            elif usuario == "s":
                print("abajo")
            elif usuario == "a":
                print("izquierda")
            elif usuario == "d":
                print("derecha")
            else:
                print("???")
def tamaño():
    gb = 1
    a = 0
    while a != -1:
        a = int(input())
        if a == -1:
            break
        else:
            if a == 0 or a == 1:
                gb = a + gb
                print("Tu tamaño es de:", gb)
            else:
                print("Numero invalido, solo puedes poner 0 o 1")
        
        
def colision_eje_x():
    posicion = 0
    muerte = 0                            #Lo uso como flag para cuando colisione terminar el ciclo.
    while muerte != -1:
        posicion = int(input())
        if posicion <= limpositivo and posicion >= limnegativo:
            print(nc)
        else:
            print(c)
            muerte = -1
        
def colision_eje_y():
    posicion = 0
    muerte = 0
    while muerte != -1:
        posicion = int(input())
        if posicion <= limpositivo and posicion >= limnegativo:
            print(nc)
        else:
            print(c)
            muerte = -1

# Agregado en Avance 6

def comida(): # Funcion que arroja dos valores random para la ubicacion de comida
    x, y = random.randint(0,15), random.randint(0,15)
    return x , y

# Creo un diccionario para que con una llave, asignarle varias "formas"
FORMAS = {    
    0: " ",       # El 0 representa que no hay nada, por eso esta vacio
    1: "o",       # El 1 representa la comida, que tendria la forma de o
    2: "●",       # El 2 representa el cuerpo de la serpiente
    }
# Creo una funcion con listas y ciclos for para crear tablero del juego
# Me adelanto un poco en matrices para crear el tablero
# En este tablero mas adelante se guardaran los datos de la posicion de serpiente y comida

def crear_grid(ancho, alto):           # dos parametros, en este caso 15 x 15
    grid = []                          # pone al grid/tablero como lista vacia
    for fila in range(alto):           # crea una lista del tamaño de alto, recorre cada "valor vacio"
        new_list = []                  # nueva lista
        for columna in range(ancho):   # crea una lista del tamaño de ancho, recorre cada "valor vacio"
            new_list.append(0)         # cada vuelta, agrega 0 
        grid.append(new_list)          # agrega la lista de 0 por cada vuelta a la lista grid (crea matriz)
    return grid

tablero = crear_grid(ANCHO, ALTO)
# Creo una funcion para en base a la anterior funcion, dibujar el tablero (matriz)

def dibujar_grid(grid):                                  # Recibe la matrix del tablero hecho en la anterior funcion
    for fila in range(len(tablero)):                     # Recorre las filas de del tablero (Matriz)
        for columna in range(len(tablero[0])):           # Recorre los valores de la columna 
            print(FORMAS[grid[fila][columna]], end=" ")  # Imprime cada valor del tablero, usando la biblioteca para los valores
        print()                                          # Salto de linea 
 
 
tablero[4][4] = 2            # Un ejemplo de como funcionan el dibujar tablero, el diccionario toma a 2 como serpiente
dibujar_grid(tablero)



("Visualiza las teclas WASD como flechas")
print("Escoge un movimiento, w, a, s, d. ")      
print("Cuando quieras salir de bucle escribe terminar")
movimientos()


print("Tu tamaño base es de 1")
print("Ganaste una bolita? Si: 1 No:0?")
print("Para terminar el bucle escribe -1")
tamaño()
                           

print("Escribe tu posicion en la eje de las x, los limites son entre 0 a 15, si los superas, colisionaras")
print("Si colisionas el ciclo terminara y mueres")
colision_eje_x()


print("Escribe tu posicion en la eje de las y, los limites son entre 0 a 15, si los superas, colisionaras")
print("Si colisionas el ciclo terminara y mueres")
colision_eje_y()


