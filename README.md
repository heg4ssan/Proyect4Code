# EaterGame

El videojuego "EaterGame" está ligeramente inspirado en el clásico juego SNAKE de nokia. El objetivo del usuario es conseguir el mayor puntaje posible con un máximo de 25 movimientos en el tablero. Esto en un tablero de 15 x 15, donde el usuario es representado como una bola, y los puntos (comida), están representados por bolas vacías. Para "Ganar" en este juego debes conseguir 7 o más puntos, si el usuario logra el anterior puntaje, será venerado y felicitado por el programa. Las instrucciones son simples, los movimientos se realizan con w, a, s y d representando las flechas, después seguir los puntos y conseguir los más posibles.

### Algoritmo

El programa funciona a base de un ciclo principal, donde se dibuja el tablero usando una matriz, se lee el movimiento del usuario, con ese dato calcula su nueva posición, revisa si en esa posición se salió del tablero (colisión), revisa si la posición del usuario coincide con la de la comida, si es así, agrega un punto a la puntuación y cambia la comida de posición por una random, y por último, actualiza el tablero con las nuevas posiciones y puntuación.

### Bibliotecas

En el código, usé solo la biblioteca random. Random es una biblioteca estándar de Python, eso quiere decir que ya viene incluida por defecto en el lenguaje y no es necesario instalar nada para usarla, esta biblioteca se usa para generar números pseudoaleatorios, se les llama así porque aunque a nuestros ojos se ven aleatorios, en realidad son generados por un algoritmo matemático. Para este juego, esa aleatoriedad es más que suficiente. En mi código la integro de la siguiente manera, random ofrece muchas funciones, pero la que fue útil para este programa fue: random.randint(a,b), esta función devuelve un número aleatorio que está entre los valores a y b, en este caso, lo usé para generar la posición de la comida. Que la comida tenga posiciones random bastante interesante, ya que vuelven al juego prácticamente de suerte, y lo hace mucho más retador y complicado. Hasta día de hoy, nadie ha conseguido más de 7 puntos debido a esta función.

### Instrucciones

Para jugarlo, descarga el archivo y córrelo en la terminal, o abre algún IDE y presiona el botón de play.

Gracias por jugar :)
