✴️ HUNDIR LA FLOTA ESTELAR 🟣 Proyecto de programación en Python

  Mediante una serie de funciones de creación de barcos y tableros, creamos un juego funcional de posicionamiento de barcos y disparos entre el jugador y la máquina.
  
  Como detalles, destacar el uso de música de fondo y de disparos y aciertos mediante Pygames, además del uso de iconos en los gráficos del tablero.
    
  El juego se compone de una serie de tableros de 10x10, diferenciandose por un lado los tableros de la máquina (el real y el que se nos muestra) y el tablero del    jugador, donde veremos los barcos que nosotros hemos posicionado y que la máquina intentará atacar.
  
  A través de una serie de inputs al usuario, se colocarán los barcos por coordenadadas y orientación. Los barcos de la máquina se colocan aleatoriamente.
  
  Respecto a los disparos, de igual manera, se pregunta al usuario que coordenadas quiere atacar, y la máquina lo efectuará a posteriori aleatoriamente.
  Si acertamos 🔥, seguimos disparando; si le damos al agua 🔵; se pasa el turno a la máquina.
  
  
  [Ejemplo visual de la versión DEMO 🎮]
  
  Bienvenido a "HUNDIR LA FLOTA ESTELAR"
  
      Hola Sara !, Bienvenida :)
      
      Las naves vienen representadas por un '🚀'
      
      El símbolo '🔷' hace referencia a un disparo fallido
      
      El símbolo '⭕' hace referencia a un barco tocado
      
      A continuación colocarás los barcos según coordenadas y orientación...
      
      CARGANDO...
      
      Colocando barco en posicion (0, 1)
      
      Colocando barco en posicion (3, 2)
      
      Colocando barco en posicion (4, 2)
      
      Colocando barco en posicion (5, 2)
      
      Colocando barco en posicion (6, 2)
      
      Colocando barco en posicion (0, 1)
      
      Colocando barco en posicion (0, 2)
      
      Colocando barco en posicion (0, 3)
      
      Colocando barco en posicion (0, 4)
      
      La máquina ha colocado todos sus barcos
      
      A continuación empezarás a disparar a las naves de la máquina
      
      [['⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '🚀' '⚪' '⚪' '⚪']
       ['⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['🚀' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['🚀' '🚀' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['🚀' '🚀' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['🚀' '🚀' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['⚪' '🚀' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']
       ['⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪' '⚪']]
