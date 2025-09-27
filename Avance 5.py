
def movimientos():                   #En este avance, defini mis tres algoritmos como funciones, y use ciclos while(avance 5) ademas tambien agregue dos funciones de colision en eje x y y 
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
            
limpositivo = 20
limnegativo = 0
        
def colision_eje_x():
    posicion = 0
    muerte = 0  #Lo uso como flag para cuando colisione terminar el ciclo.
    nc = "no colisiona"
    c = "colisiona"
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
    nc = "no colisiona"
    c = "colisiona"
    while muerte != -1:
        posicion = int(input())
        if posicion <= limpositivo and posicion >= limnegativo:
            print(nc)
        else:
            print(c)
            muerte = -1
    



print("Visualiza las teclas WASD como flechas")
print("Escoge un movimiento, w, a, s, d. ")      
print("Cuando quieras salir de bucle escribe terminar")
movimientos()


print("Tu tamaño base es de 1")
print("Ganaste una bolita? Si: 1 No:0?")
print("Para terminar el bucle escribe -1")
tamaño()
                           

print("Escribe tu posicion en la eje de las x, los limites son entre 0 a 20, si los superas, colisionaras")
print("Si colisionas el ciclo terminara y mueres")
colision_eje_x()


print("Escribe tu posicion en la eje de las y, los limites son entre 0 a 20, si los superas, colisionaras")
print("Si colisionas el ciclo terminara y mueres")
colision_eje_y()
