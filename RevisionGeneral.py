import random
 
limpositivo = 14
limnegativo = 0

ANCHO = 15
ALTO = 15


def movimientos():
    usuario = input()
    if usuario == "w":
        direccion = [-1,0]
    elif usuario == "s":
        direccion = [1,0]
    elif usuario == "a":
        direccion = [0,-1]
    elif usuario == "d":
        direccion = [0,1]
    else:
        print("Ese no es un movimiento")
        direccion = [0,0]
    return direccion

def sumlistas(lista, lista2):
    newlist = []
    for i in range(len(lista)):
        newlist.append(lista[i] + lista2[i])
    return newlist

                
def comidacheck(usuario, comida_pos):
    if usuario == comida_pos:
        return True
    else:
        return False 
    
        
def colision_eje_x(posicion):
    if posicion <= limpositivo and posicion >= limnegativo:
        muerte = False
    else:
        muerte = True
    return muerte
        

def colision_eje_y(posicion):
    if posicion <= limpositivo and posicion >= limnegativo:
        muerte = False
    else:
        muerte = True
    return muerte


def comida(): 
    x, y = random.randint(0,14), random.randint(0,14)
    return [x , y]


FORMAS = {    
    0: "-",       
    1: "o",       
    2: "●",       
    }


def crear_grid(ancho, alto):           
    grid = []                          
    for fila in range(alto):           
        new_list = []                  
        for columna in range(ancho):   
            new_list.append(0)         
        grid.append(new_list)          
    return grid


def dibujar_grid(tablero):                                  
    for fila in range(len(tablero)):                     
        for columna in range(len(tablero[0])):            
            print(FORMAS[tablero[fila][columna]], end=" ")  
        print()
        
    
tablero = crear_grid(ANCHO, ALTO)



"""
Funcion Main:
Primero imprime con condiciones iniciales, luego en un ciclo while, borra la posicion anterior del usuario, luego lee el movimiento que tecleo 
el usuario, usando operadores aritmeticos para hacerlo mover dependiendo el movimiento, despues las colisiones, si el usuario se salio del mimite y o del limite x, si se salio, termina el ciclo\
tambien se revisa cuantos movimientos le quedan al usuario (max 25), si son mas, termina el ciclo, despues revisa si el usuario esta en la misma posicion que la comida, si lo esta, crea otra
posicion para la comida, borra la anterior y suma un punto al contador, despues actualiza la posicion del usuario y comida, y se imprime el nuevo tablero con nuevas posiciones y nueva puntuacion 
deapues pongo que el contador de movimientos solo aumente si el usuario si presiono una tecla de movimiento\dirrecion, por ultimo con un pequeno if, reviso cuantos puntos saco el usuario
y le pone un mensaje dependiendo eso

"""

def main():
    
    usuario = [5,5]
    comida_pos = [6,7]
    direccion = [0,0]
    puntuacion = 0
    gameover = False
    tablero[usuario[0]][usuario[1]] = 2
    tablero[comida_pos[0]][comida_pos[1]]= 1
    dibujar_grid(tablero)
    cont = 1
    
    while gameover == False:

        tablero[usuario[0]][usuario[1]] = 0
        
        direccion = movimientos()
        usuario = sumlistas(usuario, direccion)
        
        if colision_eje_x(usuario[0]) or colision_eje_y(usuario[1]) == True:
            gameover = True
            break
        if cont > 25:
            gameover = True
            break
        
        if comidacheck(usuario, comida_pos) == True:
            puntuacion = puntuacion + 1
            tablero[comida_pos[0]][comida_pos[1]]= 0
            comida_pos = comida()
        
        tablero[usuario[0]][usuario[1]] = 2
        tablero[comida_pos[0]][comida_pos[1]]= 1
        
        dibujar_grid(tablero)
        
        print("Puntos:", puntuacion,)
        
        if direccion != [0,0]:
            cont = cont + 1
    
    print("Tu puntuaje fue de", puntuacion)
    if puntuacion < 5:
        print("Nada mal, nada mal...")
    elif puntuacion >= 5 and puntuacion < 7:
        print("Casi lo logras! te falto solo un poco")
    elif puntuacion >= 7:
        print("Los dioses del olimpo te admiran, lo que lograste fue una en un millon.")
        
            
print("Bienvenido viajero!")
print("Lo que estas viendo es el tablero, y esa bola negra eres tu!")
print("Ves esa bola vacia?, es tu objetivo.")
print("Tienes que conseguir las que mas puedas.")
print("Pero ojo! solo tienes 25 movimientos, asi que usalos de manera inteligente.")
print("Cuidado con salirte del tablero, moriras!")
print("Si consigues 7 o mas, tienes el respeto de los dioses del olimpo.")
print("Vamos, intentalo! te mueves con w, a, s, d.")
print("Buena suerte viajero.")
main()