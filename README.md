# Proyect4Code
Este proyecto será un programa inspirado en el clásico video juego “Snake” de Nokia, en donde el objetivo del juego es aumentar la longitud de tu serpiente lo más posible, alimentándola con manzanas (bolas) distribuidas aleatoreamente en el cuadro, donde cada vez que comas una, otra aparecerá.
El juego tiene un contador de puntos, el cual dira la cantidad de manzanas (bolas) que tu serpiente ha consumido. Si chocas con un extremo del cuadro, perderás la partida, reiniciando el juego.
Este proyecto es interesante debido a que revive la nostalgia y la magia de este clásico juego. 
Personalmente es un desafío retador e insipardor para aprender más sobre programación.



Algoritmo:

Inicio
mover arriba = teclear_W
	Si teclear_W = mover arriba
                SI NO teclear_W = mantener 
 mover abajo = teclear_S
	Si teclear_S = mover abajo 
                SI NO teclear_S = mantener 
   mover derecha = teclear_D
	Si teclear_D = mover derecha
                SI NO teclear_D = mantener 
     mover izquierda = teclear_A
	Si teclear_A = mover izquierda 
                SI NO teclear_A= mantener 
    Fin Si
        ganar_bolita = crecer
           SI = “ganar bolita” = crecer
		SI NO = “ganar bolita” =  mantener_tamaño 
    Fin Si 
          vivir = (“ganar bolitas y no chocar”)
	SI = “ganar bolitas y no chocar” = vivir 
		SI NO = “ganar bolitas y no chocar” = morir
    Fin Si 
Fin 
