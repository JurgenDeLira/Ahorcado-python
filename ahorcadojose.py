import random # Importamos la libreria "random"

def mostrar_ahorcado(intentos, dificultad):
    etapas_6 = [
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
             ]

    etapas_8 = [
    '''
                --------
                |      |
                |      
                |    
                |      
                |     
                -
    ''',
    '''
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
    ''',
    '''
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
    ''',
    '''
                --------
                |      |
                |      O
                |      |\\
                |      
                |     
                -
    ''',
    '''
                --------
                |      |
                |      O
                |      |\\
                |      
                |     
                -
    ''',
    '''
                --------
                |      |
                |      O
                |     /|\\
                |      
                |     
                -

    ''',
    '''
                --------
                |      |
                |      O
                |     /|\\
                |      |
                |     / 
                -
    ''',
    '''
                --------
                |      |
                |      O
                |     /|\\
                |      |
                |     / \\
                - 
    ''',
    '''
                --------
                |      |
                |      O
                |    _/|\\_
                |      |
                |     / \\
                -
    ''']
    
    etapas_12 = [
        '''
                --------
                |      |
                |      
                |    
                |      
                |     
                -
        ''',
        '''
                --------
                |      |
                |      
                |      O
                |    
                |     
                -
        ''',
        '''
                --------
                |      |
                |      O
                |      
                |    
                |     
                -
        ''',
        '''
                --------
                |      |
                |      O
                |      |
                |    
                |     
                -
        ''',
        '''
                --------
                |      |
                |      O
                |     /|
                |    
                |     
                -
        ''',
        '''
                --------
                |      |
                |      O
                |     /|\\
                |    
                |     
                -
        ''',
        '''
                --------
                |      |
                |      O
                |     /|\\
                |      |
                |    
                -

        ''',
        '''
                --------
                |      |
                |      O
                |     /|\\
                |      |
                |     / 
                -
        ''',
        '''
                --------
                |      |
                |      O
                |     /|\\
                |      |
                |     / \\
                -
        ''',
        '''
                --------
                |      |
                |      O
                |    _/|\\
                |      |
                |     / \\
                -

        ''',
        '''
                --------
                |      |
                |      O
                |    _/|\\_
                |      |
                |     / \\
                -
        ''',
        '''
                --------
                |      |
                |      O
                |    _/|\\_
                |      |
                |     / \\
                |    
                -
        ''',
        '''
                --------
                |      |
                |      O
                |    _/|\\_
                |      |
                |    _/ \\_
                |    
                -
        ''',

    ]

    etapas_8 = etapas_8[::-1]

    etapas_12 = etapas_12[::-1]


    if dificultad == 1:
        return etapas_6[intentos]
    elif dificultad == 2:
        return etapas_8[intentos]
    else:
        return etapas_12[intentos]


# -----------------------------------------------------------

def seleccionar_palabra(): # Función que nos retornará una palabra al azar
  palabras = [] # Esta lista alamacenará las palabras a adivinar
  
  numero_palabras = int(input('Ingresa la cantidad de palabras para jugar: '))

  for i in range(0,numero_palabras): # Creamos un ciclo donde se pueda pedir palabras al usuario
    palabra_usuario = input(f'Ingresa la palabra {i + 1}: ') # Pedimos una palabra 

    palabras.append(palabra_usuario.lower()) # Agremos esa nueva palabra al final de la lista

  palabra_aleatoria = random.choice(palabras) # Elegimos una palabra aleatoria

  return palabra_aleatoria # La función retorna una palabra al azar

# -----------------------------------------------------------

# -----------------------------------------------------------


def mostrar_tablero(palabra_secreta, letras_adivinadas): # Dependiendo de la palabra, la función "dibujará" un tablero
  tablero = '' # Esta variable nos servirá para mostrar el tablero
  for letra in palabra_secreta:
    if letra in letras_adivinadas:
      tablero += letra
    else:
      tablero += '_'
    tablero += ' '
  
  return tablero
# -----------------------------------------------------------



# -----------------------------------------------------------
def juego_ahorcado(): # En esta función se ejecutará el juego como tal
  palabra_secreta = seleccionar_palabra() # Creamos una variable que almacena la palabra secreta elegida por nuestra función
  letras_adivinadas_usuario = set() # Creamos un conjunto que almacene las letras del usuario
  dificultad = 0

  if len(palabra_secreta) >= 12:
    intentos = 12
    dificultad = 3

  elif len(palabra_secreta) >= 8:
    intentos = 8
    dificultad = 2
  else:
    intentos = 6
    dificultad = 1
  
  # Le damos la bienvenida y dibujamos el tablero principal
  print('------ Bienvenid@ al juego del ahorcado ------')
  print(f'Tienes {intentos} intentos') # Mostramos los intentos
  print('\n')
  print(mostrar_tablero(palabra_secreta, letras_adivinadas_usuario))
  print(mostrar_ahorcado(intentos, dificultad))
  print('\n')


  # Creamos un ciclo que se ejecute mientras el usuario aun tenga vidas y que el conjunto de palabra_secreta NO sea subconjunto de palabras_adivinadas por el usuario
  while intentos > 0 and not set(palabra_secreta).issubset(letras_adivinadas_usuario):

    letra_adivinada = input('Escribe la letra que te gustaria adivinar: ').lower() # Le pedimos al usuario una letra para adivinar
 
    if letra_adivinada in letras_adivinadas_usuario: # Comparamos si la palabra_adivinada está en el conjunto letras_adivnidas_usuario
      intentos -= 1 # Restamos una vida
      print('Oye, esta letra ya la adivinaste, intenta con otra') # Regañamos al usuario
      print(f'Tienes {intentos} intentos') # Mostramos los intentos

    elif letra_adivinada in palabra_secreta: # Comparamos si la letra_adivinada está en la palabra_secreta
      letras_adivinadas_usuario.add(letra_adivinada) # Agregamos la palabra al conjunto letras_adivinadas_usuario
      print('Bien hecho!') # Felicitamos al usuario
    
    else: # Si la palabra no está ni repetida ni en palabra_secreta
      intentos -= 1 # Restamos una vida
      print('Lo siento esta letra no esta')  # Regañamos al usuario
      print(f'Tienes {intentos} intentos') # Mostramos los intentos
      letras_adivinadas_usuario.add(letra_adivinada) # Agregamos la palabra al conjunto letras_adivinadas_usuario

    # Mostramos el tablero actualizado
    print(mostrar_tablero(palabra_secreta, letras_adivinadas_usuario))
    print(mostrar_ahorcado(intentos, dificultad))
    print('\n')
  

  if (intentos == 0):
    print(f'''
      -----------------------------------------------------------
        Lo sentimos, perdiste el juego.
        La palabra que no pudiste adivinar fue: {palabra_secreta}
      -----------------------------------------------------------
    ''')
  else:
    print(f'''
      -----------------------------------------------------------
        Felicidades!!! has adivinado la palabra secreta :D
          
                    Toma pastel de regalo
          

                          ~                  ~
          *                   *                *       *
                        *               *
        ~       *                *         ~    *
                    *       ~        *              *   ~
                        )         (         )              *
          *    ~     ) (_)   (   (_)   )   (_) (  *
                *  (_) # ) (_) ) # ( (_) ( # (_)       *
                    _#.-#(_)-#-(_)#(_)-#-(_)#-.#_
        *         .' #  # #  #  # # #  #  # #  # `.   ~     *
                :   #    #  #  #   #  #  #    #   :
          ~      :.       #     #   #     #       .:      *
              *  | `-.__                     __.-' | *
                |      `````"""""""""""`````      |         *
          *     |         | ||\ |~)|~)\ /         |
                |         |~||~\|~ |~  |          |       ~
        ~   *   |                                 | *
                |      |~)||~)~|~| ||~\|\ \ /     |         *
        *    _.-|      |~)||~\ | |~|| /|~\ |      |-._
            .'   '.      ~            ~           .'   `.  *
            :      `-.__                     __.-'      :
            `.         `````"""""""""""`````         .'
              `-.._                             _..-'
                    `````""""-----------""""`````
      -----------------------------------------------------------
    ''')


# -----------------------------------------------------------


# Se ejecuta la función principal
juego_ahorcado()



