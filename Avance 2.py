
print("Visualiza las teclas WASD como flechas")
print("Escoje un movimiento, w:1 a:2 s:3 d:4 ")
movimientos = ["arriba", "izquierda", "abajo", "derecha"] #Se usa una lista para asignarle variables a los movimientos.
a = int(input()) #Le pide un número del 1 al 4 al usuario
movimiento = movimientos[a - 1] #Se usa el operador aritmético de - por que la lista empieza a valorar con 0, no en 1.
print(movimiento)               #Asi el numero dado por el usuario se resta con 1 y regresa el movimiento correcto de la lista. 
b = int(input())
movimiento = movimientos[b - 1] #Se repite lo anterior 3 veces mas para una muestra de rango de movimiento completo.
print(movimiento)
c = int(input())
movimiento = movimientos[c - 1]
print(movimiento)
d = int(input())
movimiento = movimientos[d - 1]
print(movimiento)
#En proximos avances se pondran ciclos para que el jugador se mueva infinitamente, no solo 4 veces.