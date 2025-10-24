"""
Proyecto final
Juego inspirado en snake
El programa es un juego parecido al clasico snake de nokia
pero con algunas modificaciones, tienes un limite de movimientos
y debes intentar lograr ciertos puntos
"""

# bibliotecas
import random
 
# variables globales
LIM_POSITIVO = 14
LIM_NEGATIVO = 0
LIM_MOVIMIENTOS = 25
ANCHO = 15
ALTO = 15


"""
    diccionario que le asigna a un numero(llave), a diferentes formas
    (valores).
"""
FORMAS = {    
    0: "-",       
    1: "o",       
    2: "●",       
    }


#========================= funciones principales =======================


def movimientos(usuario):
    """
    (uso de condiciones, funciones)
    recibe: usuario / string pedido al usuario con su movimiento
    funcion que lee el movimiento escrito por el usuario y 
    dependiendo cual elija, se guarda un el movimiento en una variable
    (dirrecion), que es una lista con movimiento basado en 
    el eje de x y y.
    devuelve: variable que guarda el movimiento
    """
    if usuario == "w":
        direccion = [-1, 0]
    elif usuario == "s":
        direccion = [1, 0]
    elif usuario == "a":
        direccion = [0, -1]
    elif usuario == "d":
        direccion = [0, 1]
    else:
        print("Ese no es un movimiento")
        direccion = [0, 0]
    return direccion


def sumlistas(lista, lista2):
    """
    (uso de listas, ciclos for)
    recibe: dos listas
    funcion que se usa para sumar los valores de dos listas del 
    mismo tamaño y agregarlos a una nueva lista.
    devuelve: nueva lista 
    """
    newlist = []
    for i in range(len(lista)):
        newlist.append(lista[i] + lista2[i])
    return newlist

                
def comidacheck(usuario, comida_pos):
    """
    recibe: la cordenada/lista, actual del usuario, la posicion 
    actual de la comida
    funcion que compara si la cordenada del usuario es la misma 
    que la de la comida
    devuelve: verdadero o falso, dependiendo si se cumple la 
    funcion o no
    """
    if usuario == comida_pos:
        return True
    else:
        return False 
    
        
def colision_eje_x(posicion):
    """
    (uso de operadores)
    recibe: la posicion actual del usuario
    funcion que revisa si el usuario esta dentro del tablero en el
    eje de las x, usando las variables globales de limites,si la
    posicion supera el limites, la funcion devuelve True, de lo 
    contrario, False.
    devuelve: True o False 
    """
    if posicion <= LIM_POSITIVO and posicion >= LIM_NEGATIVO:
        muerte = False
    else:
        muerte = True
    return muerte
        

def colision_eje_y(posicion):
    """
    recibe: la posicion actual del usuario
    funcion que revisa si el usuario esta dentro del tablero en 
    el eje de la y, usando las variables globales de limites,si la
    posicion supera el limites, la funcion devuelve True, de lo 
    contrario, False.
    devuelve: True o False 
    """
    if posicion <= LIM_POSITIVO and posicion >= LIM_NEGATIVO:
        muerte = False
    else:
        muerte = True
    return muerte


def comida(): 
    """
    funcion que devuelve dos posiciones, x y y, randomizados por la 
    biblioteca random.
    devuelve: x y y ranodmizados
    """
    x, y = random.randint(0, 14), random.randint(0, 14)
    return [x, y]


def crear_grid(ancho, alto):          
    """
    (matrices, ciclos for)
    recibe: el ancho y alto del tablero.
    funcion que crea una matriz que representra al tablero, creando
    una nueva lista por cada fila y agregando esa lista con 0 a la 
    lista de grid por cada columna.
    devuelve: una matriz que representa el tablero
    """
    grid = []                          
    for fila in range(alto):           
        new_list = []                  
        for columna in range(ancho):   
            new_list.append(0)         
        grid.append(new_list)          
    return grid


def dibujar_grid(tablero):
    """
    recibe: la matriz creada en la funcion aterior.
    funcion que recorre las filas y columnas del tablero, y usa el 
    diccionario para cambiar los numeros "llaves" por las formas
    "valores".

    """                                  
    for fila in range(len(tablero)):                     
        for columna in range(len(tablero[0])):            
            print(FORMAS[tablero[fila][columna]], end=" ")  
        print()
        

#=========================== funcion del juego ==========================


def partida(tablero):
    """
    recibe: tablero 
    Esta función inicializa las variables del juego como la
    posicion del jugador, la comida, y maneja el bucle de juego.
    En cada turno, lee el movimiento del usuario, actualiza las
    posiciones, detecta colisiones (comida y bordes) y revisa el
    limite de movimientos.
    El juego termina cuando se cumple una la condicion de 'gameover'.
    El algoritmo del juego se basa en esta funcion (readme)
    devuelve: puntuacion final
    """
    usuario = [5, 5]
    comida_pos = [6, 7]
    direccion = [0, 0]
    puntuacion = 0
    gameover = False
    tablero[usuario[0]][usuario[1]] = 2
    tablero[comida_pos[0]][comida_pos[1]] = 1
    dibujar_grid(tablero)
    movimientos_realizados = 1
    
    while not gameover:

        tablero[usuario[0]][usuario[1]] = 0
        movimiento = input()
        direccion = movimientos(movimiento)
        usuario = sumlistas(usuario, direccion)
        
        if colision_eje_x(usuario[0]) or colision_eje_y(usuario[1]):
            gameover = True
            
        elif movimientos_realizados > LIM_MOVIMIENTOS:
            gameover = True

        if not gameover:    
        
            if comidacheck(usuario, comida_pos):
                puntuacion += 1
                tablero[comida_pos[0]][comida_pos[1]] = 0
                comida_pos = comida()
        
            tablero[usuario[0]][usuario[1]] = 2
            tablero[comida_pos[0]][comida_pos[1]] = 1
        
            dibujar_grid(tablero)
        
            print("Puntos:", puntuacion,)
        
            if direccion != [0, 0]:
                movimientos_realizados += 1
    
    return puntuacion


#=========================== funcion main =============================


def main():
    """
    funcion que imprime mensaje inicial, crea el tablero, y ese 
    tablero se usa para correr el juego principal, una ves terminado
    el juego, la puntuacion se guarda y dependiendo de ella, sale
    un mensaje
    """
    print("Bienvenido viajero!")
    print("Lo que estas viendo es el tablero, y esa bola negra eres tu!")
    print("Ves esa bola vacia?, es tu objetivo.")
    print("Tienes que conseguir las que mas puedas.")
    print("Pero ojo! solo tienes 25 movimientos, asi que usalos de manera "
        "inteligente.")
    print("Cuidado con salirte del tablero, moriras!")
    print("Si consigues 7 o mas, tienes el respeto de los "
        "dioses del olimpo.")
    print("Vamos, intentalo! te mueves con w, a, s, d.")
    print("Buena suerte viajero.")

    tablero = crear_grid(ANCHO, ALTO)

    puntuacion = partida(tablero)
            

    print("Tu puntuaje fue de", puntuacion)
    if puntuacion < 5:
        print("Nada mal, nada mal...")
    elif puntuacion >= 5 and puntuacion < 7:
        print("Casi lo logras! te falto solo un poco")
    elif puntuacion >= 7:
        print("Los dioses del olimpo te admiran, lo que lograste fue "
            "una en un millon.")

main()
