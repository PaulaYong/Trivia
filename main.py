#Importar librerias
import time
import random

#Variables fijas de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Variables fijas de estilo
BRIGHT = '\033[1m'
DIM = '\033[2m'
NORMAL = '\033[22m'
RESET_ALL = '\033[0m'

#Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(DIM+'Bienvenido a mi trivia sobre back-end!')
print('Pondremos a prueba tus conocimientos')
time.sleep(1) # Espera 1 segundos antes de continuar.

#Agregaremos personalización consultando nombre
nombre = input(BRIGHT+'\nIngresa tu nombre: '+RESET_ALL)

print(DIM+'\nHola',nombre, 'responde las siguientes preguntas escribiendo la letra de la alternativa y presionando "Enter" para enviar tu respuesta.\n')
time.sleep(1)

#Oportunidades que tiene el juegador
oportunidades = 1
print('Tienes', oportunidades,'oportunidad de responder correctamente a cada pregunta.Por favor, pon tu respuesta:\n'+RESET_ALL)
time.sleep(2)

#Score del jugador
score = 0

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 8)

#Pregunta 1
pregunta_1 = print(CYAN+'1) ¿Qué es un desarrollador back-end?'+RESET)
print(DIM+'a) En la parte del desarrollo web es la persona que se dedica a la parte frontal de un sitio web, en pocas palabras del diseño de un sitio web, desde la estructura del sitio hasta los estilos como colores, fondos, tamaños hasta llegar a las animaciones y efectos.'
)
print('b) Es la persona encargada de la implementación de un sitio web o aplicación web en todos sus componentes, y se ocupa de diseñar la lógica y las soluciones para que las acciones solicitadas en un sitio o aplicación web sean ejecutadas correctamente.'+RESET_ALL)

respuesta_1 = 'b'

#Bucle While
while respuesta_1 not in ('a', 'b', 'c', 'd'):
  respuesta_1 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

#Bucle for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Pon tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_1):
        print(YELLOW+'Correcto! Buen trabajo.\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
      
        break
    else:
        print(RED+'Incorrecto! La siguiente lo harás mejor\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print('La respuesta correcta es', respuesta_1, '\n\n'+RESET)

time.sleep(2)

#Pregunta 2
pregunta_2 = print(CYAN+'2) ¿Cúal es un lenguale del lado del Back-end?'+RESET)
print(DIM+'a) HTML')
print('b) CSS')
print('c) JavaScript')
print('d) Python'+RESET_ALL)

respuesta_2 = 'd'

#Bucle for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Pon tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_2):
        print(YELLOW+'Correcto! Eres un genio.\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
        break
    else:
        print(RED+'Incorrecto! No te desanimes\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print('La respuesta correcta es', respuesta_2,'Los lenguajes utilizados para el back-end incluyen Java, Ruby, Python''\n\n'+RESET)

time.sleep(2)

#Pregunta 3
pregunta_3 = print(CYAN+'3) ¿Cúal no es un lenguale del lado del Back-end?'+RESET)
print(DIM+'a) Python')
print('b) CSS')
print('c) Java')
print('d) Ruby'+RESET_ALL)

respuesta_3 = 'b'

#Bucle for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Pon tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_3):
        print(YELLOW+'Correcto! Eres un experto\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
        break
    else:
        print(RED+'Incorrecto!Da una repasada un poco más\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print('La respuesta correcta es', respuesta_3,'HTML, CSS y JavaScript son los lenguajes utilizados para el desarrollo de Front End.''\n\n'+RESET)

time.sleep(2)

#Pregunta 4
pregunta_4 = print(CYAN+'4) ¿Cúal no software de bases de datos o DBMS?'+RESET)
print(DIM+'a) MySQL')
print('b) Oracle Database')
print('c) PostgreSQL')
print('d) Ruby Database'+RESET_ALL)

respuesta_4 = 'd'

#Bucle for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Pon tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_4):
        print(YELLOW+'Correcto! Eres un master.\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
        break
    else:
        print(RED+'Incorrecto!Repasando mejorarás\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print("La respuesta correcta es", respuesta_4,'Ruby Database no existe''\n\n'+RESET)

time.sleep(1)

#Imrpime el puntaje obtenido
while score >= 3:
    print(YELLOW+BRIGHT+'¡Bien hecho!', nombre, 'tu aciertos son', score,'y tienes', puntaje, 'puntos')
    break

while score <= 2:
    print(RED+'¡Mejor suerte la próxima vez!', nombre, 'tus aciertos fueron', score, 'tu puntaje fue', puntaje,'puntos')
    break

#Mensaje de despedida
print(CYAN+'¡Gracias por jugar la trivia de back-end!'+RESET_ALL)
