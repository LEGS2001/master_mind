import random

# Variables
jugadores = []
puntajes = []
intentos = []
partida = []
npartida = []
salir = "no"
numero = ""

#Generar numero
def Generador():
    global numero
    numero = ""
    while (len(numero) < 4):
            num = random.randint(0,9)
            num = str(num)
            if num not in numero:
                numero = numero + num               

#Adivinar
def Juego():
    continuar = "Si"
    print("Partida #", npartida[njugador])
    while (puntajes[njugador] > 0):
        if (continuar == "Si" or continuar == "si"):
            print("Intento No.", intentos[njugador])
            apuesta = int(input("Ingrese una apuesta entre 1 y 5 \n"))
            if (apuesta >= 1 and apuesta <= 5):
                respuesta = str(input("Ingrese un numero de 4 digitos \n"))
                if (numero == respuesta):
                        print("Ha adivinado el numero correctamente")
                        puntajes[njugador] = puntajes[njugador] + apuesta 
                        print("Su puntaje es:", puntajes[njugador])
                        intentos[njugador] = intentos[njugador] + 1
                        Generador()                       
                else:
                    puntajes[njugador] = puntajes[njugador] - apuesta 
                    intentos[njugador] = intentos[njugador] + 1
                    print("Su puntaje es:", puntajes[njugador])
                    if (puntajes[njugador] <= 0):
                        print("Se ha quedado sin puntos")
                        partida[njugador] = "Finalizada"
                        break
                    for i in range (0, 4):
                        if (numero[i] == respuesta[i]):
                            print("Coincidencias en valor y posicion:", respuesta[i]) 
                        else:
                            for x in respuesta:
                                if (x == numero[i]):
                                    print("Coincidencias solo en valor:", x)   
                                    
                continuar = input("Desea continuar? Si/No \n")                                                                
        else:
            break
        
while (salir == "no"):

#Menu
    print("1) Iniciar partida \n2) Reiniciar partida \n3) Ver tabla de jugadores \n4) Salir")
    opcion = int(input("Ingrese un numero para la opcion deseada \n"))

#Reiniciar Partida
    if (opcion == 2):
        jugador = input("Ingrese el jugador con el que quiere reanudar su partida \n")
        if (jugador not in jugadores):
            print("El jugador no existe")
            continue
        else:
            njugador = jugadores.index(jugador)
            if (puntajes[njugador] <= 0):
                print("Este jugador ha sido eliminado")
                continue
            npartida[njugador] = npartida[njugador] + 1
            Generador()
            Juego()

#Iniciar Partida
    if (opcion == 1):
        if (len(jugadores) < 5):
            jugador = input("Ingrese sus iniciales \n")

            #Jugador repetido
            if jugador in jugadores:
                print("El jugador ya existe, debe reiniciar o terminar la partida")
                continue
            else:
                jugadores.append(jugador)        
                puntajes.append(100) 
                partida.append("Pausada")  
                intentos.append(1)    
                npartida.append(1)  
                njugador = jugadores.index(jugador)
        else:
            print("Se ha alcanzado el numero maximo de jugadores")
            continue
    #JUEGO        
        Generador()
        Juego()
                
#Tabla de Jugadores
    if (opcion == 3):
        for i in range(0, len(jugadores)):
            print("Jugador:", jugadores[i], "; Puntaje:", puntajes[i], "; Intento:", intentos[i], "; Numero de Partidas:", npartida[i], "; Partida:", partida[i])
        

#Salir
    if (opcion == 4):
        salir = "si"
