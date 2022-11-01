tablero = ["-", "-","-",
        "-","-","-",
        "-","-","-",]

jugador = "X"

juego = True

def printTablero(tablero):
    print(tablero[0] + " | " + tablero[1] + " | "+ tablero[2])
    print("----------")
    print(tablero[3] + " | " + tablero[4] + " | "+ tablero[5])
    print("----------")
    print(tablero[6] + " | " + tablero[7] + " | "+ tablero[8])

def moviemientoJugador(tablero):
    movimiento = int(input("Elegi un lugar 1-9: ", ))
    if movimiento >= 1 and movimiento <= 9 and tablero[movimiento - 1] == "-":
        tablero[movimiento - 1] = jugador
    else:
        print("No se puede pa")
        moviemientoJugador(tablero)


def prueba(tablero,jugador):
    global juego
    if tablero[0] == tablero[1] == tablero[2] == jugador or tablero[3] == tablero[4] == tablero[5] == jugador or tablero[6] == tablero[7] == tablero[8] == jugador:
        print("-.-.-.-.-.-.-.-.-.-")
        printTablero(tablero)
        print("Gano el jugador",jugador+"!")
        juego = False
    elif tablero[0] == tablero[3] == tablero[6] == jugador or tablero[1] == tablero[4] == tablero[7] == jugador or tablero[2] == tablero[5] == tablero[8] == jugador:
        print("-.-.-.-.-.-.-.-.-.-")
        printTablero(tablero)
        print("Gano el jugador",jugador+"!")
        juego = False
    elif tablero[0] == tablero[4] == tablero[8] == jugador or tablero[2] == tablero[4] == tablero[6] == jugador:
        print("-.-.-.-.-.-.-.-.-.-")
        printTablero(tablero)
        print("Gano el jugador",jugador+"!")
        juego = False


def pruebaEmpate():
    global juego
    if "-" not in tablero and juego == True:
        print("-.-.-.-.-.-.-.-.-.-")
        printTablero(tablero)
        print("Empate!")
        juego = False

def cambioDeJugador():
    global jugador 
    if jugador == "X":
        jugador = "O"
    elif jugador == "O":
        jugador = "X"

while juego:
    printTablero(tablero)
    moviemientoJugador(tablero)
    prueba(tablero, jugador)
    pruebaEmpate()
    cambioDeJugador()