"""

"""
from random import randint

#Se establecen las dimensiones del tablero
rows = 7
cols = 8

# Se crea un tablero con las dimensiones especificadas en las variables globales rows y cols
def crearTablero():
    global rows
    global cols
    #Se llena el tablero con  "•" y se agregar 2 columnas y 1 fila para los bordes
    tablero = [["•" for _ in range(cols+2)] for _ in range(rows+1)]

    #En este for se escriben los bordes
    for i in range((rows+1)):
        for j in range((cols+2)):
            if (j == 0 or j == cols+1) and i < (rows):
                tablero[i][j]="|"
            if i == rows:
                tablero[i][j]="-"
    tablero.append(["|"])

    #En este for se escriben las columnas del tablero
    for n in range(1,cols+1):
        tablero[-1].append(str(n))
    tablero[-1].append("|")
    #regresa el tablero a una variable
    return tablero

#Esta funcion muestra en tablero con for anidado que itera la matriz
def mostrarTablero(tablero):
    for filas in tablero:
        for columnas in filas:
            print(f"{columnas}  ",end="")
        print()

#Esta funcion recibe 3 parametros, el tablero, la columna y el turno y 
# regresa si el turno puede seguir o debe de repetirse el turno
def soltarFicha(tablero, columna, turno):
    fila = 0
    #Este if automaticamente detecta si la columna esta llena ya que no esta vacio el espacio
    if tablero[0][columna] != "•": # Si la columna no esta llena encuentra el primer espacio que no este vacio, regresa 1 y mete la ficha
        print(f"Columa llena")
        return False, fila
    else:
        while tablero[fila][columna] == "•":
            fila += 1
        fila-=1
        tablero[fila][columna]=turno
        return True, fila #regresa la fila y que el juego puede seguir
    
    # Esta funcion recibe los parametros de fila columna turno y tablero
def ganar(fila, columna, turno, tablero):
    # este for utiliza un while en cada a para verificar que no haya una victoria en las 4 direcciones posibles
    for a in range(4):
        contador = 1
        i, j, k = 0,0,0
        if a == 0:
            i = fila-1
            k = fila+1
            j = columna
            while True:
                if (tablero[i][j] != turno and tablero[k][j]!=turno): break
                elif (tablero[i][j] == turno ):
                    contador += 1
                    i -= 1
                elif (tablero[k][j] == turno ):
                    contador += 1
                    k += 1
                if (contador == 4):
                    return True
        elif a == 1:
            i = columna-1
            k = columna+1
            j = fila
            while True:
                if (tablero[j][i] != turno and tablero[j][k]!=turno): break
                elif (tablero[j][i] == turno ):
                    contador += 1
                    i -= 1
                elif (tablero[j][k] == turno ):
                    contador += 1
                    k += 1
                if (contador == 4):
                    return True
        elif a == 2:
            i = columna+1
            k = fila+1
            j = fila -1
            l =  columna -1
            while True:
                if (tablero[k][i] != turno and tablero[j][l]!=turno): break
                elif (tablero[k][i] == turno ):
                    contador += 1
                    k += 1
                    i += 1
                elif (tablero[j][l] == turno ):
                    contador += 1
                    j -= 1
                    l -= 1
                if (contador == 4):
                    return True
                
        elif a == 3:
            i = columna-1
            k = fila+1
            j = fila - 1
            l = columna + 1
            while True:
                if (tablero[k][i] != turno and tablero[j][l]!=turno): break
                elif (tablero[k][i] == turno ):
                    contador += 1
                    k += 1
                    i -= 1
                elif (tablero[j][l] == turno ):
                    contador += 1
                    j -= 1
                    l += 1
                if (contador == 4):
                    return True
    return False

#Este for anidado imprime la matriz del historial
def printHistorial(historial):
    print("|  [X]  |  [O]  |")
    for filas in historial:
        print("|",end="")
        for columnas in filas:
            print(f"{columnas} |", end="")
        print("\n")

#Imprime el menu de opciones
def menu():
    print("""\n\nBienvenido a Conecta 4. Selecciona un opcion del menu
          

[1]Jugar
[2]Consultar record
[3]Borrar borrar record
[4]Salir""")
    
    
#Creacion del main
def main():
    #variables iniciales
    global rows
    global cols
    historial = []
    nTurno = 0
    turnos = ["X","O"]
    turno = ""
    tablero = crearTablero()
    empate = False


    #ciclo principal del menu
    while True:
        menu()

        #seleccion del menu
        try:
            seleccionMenu = int(input("\n"))
        except:
            print("\n\nSeleccione una opcion correcta")
            continue
        
        match seleccionMenu:
            case 1:
                #Reseteo de variables
                empate = False
                tablero = crearTablero()
                nTurno = 0
                historial = []
                #Seleccion de jugadores
                while True:
                    print("Seleccione un modo de juego\n[1]Un jugador\n[2]Dos jugadores")
                    try:
                        numeroJugadores = int(input("\n"))
                    except:
                        print("\n\nSeleccione una opcion correcta")
                        continue
                    if numeroJugadores<=2 and numeroJugadores>=1: break
                    else: 
                        print("\n\nSeleccione una opcion correcta")
                        continue
                #While del juego
                while True:
                    print("\n\n")
                    mostrarTablero(tablero)
                    #Selecciona a quien le toca si es par o impar el numero de turno
                    turno = turnos[nTurno%2]

                    #Si el numero de jugadores es 1 juega de manera aleatoria el segundo jugador
                    if  numeroJugadores == 1:
                        if turno == "X":
                            try:
                                columna =  int(input(f"\n\n{nTurno} Turno \"{turno}\" Selecciona una columa: "))
                                
                            except:
                                print("Selecciona un valor valido")
                                continue
                        elif turno =="O":
                            columna = randint(1,9)
                            print("\n\n")
                    #sino cada jugador elige su tiro
                    else:
                        try:
                            columna = int(input(f"\n\n{nTurno} Turno \"{turno}\" Selecciona una columa: "))
                            
                        except:
                            print("Selecciona un valor valido")
                            continue
                    
                    #Validacion de la columna
                    if columna < 1 or columna > cols:
                        print("\n\nColumna no valida")
                        continue
                    

                    estado, fila = soltarFicha(tablero, columna, turno)


                    if estado == False: 
                        continue
                    
                    #Actualizacion del historial
                    if nTurno%2 == 0:
                        historial.append([(fila,columna)])
                    elif nTurno%2 == 1:
                        historial[nTurno//2].append((fila,columna))
                        
                    estadoJuego = ganar(fila, columna, turno, tablero)
                    if estadoJuego: 
                        break

                    nTurno += 1

                    if nTurno == (rows*cols):
                        empate = True
                        break
                
                mostrarTablero(tablero)

                #se escoge que imprimir en base a quien gano o si se empata y se actualiza el record
                if empate == True:
                    print(f"\n\nEmpate\n\n")
                    with open("Record.txt", "a") as f:
                        f.write("Empate\n")
                        
                else:
                    print(f"\n\nGana Jugador {turno}\n\n")
                    with open("Record.txt", "a") as f:
                        f.write(f"Gana jugador {turno}\n")
            
                #Ciclo para mostrar el historial y validar la entrada de seleccion
                while True:
                    try:
                        historialYN = input("Quiere mostrar el historial de movimientos del juego?(y/n): ")
                    except:
                        print("\n\nSeleccione un valor valido")
                        continue
                    match historialYN:
                        case "y":
                            printHistorial(historial)
                            break
                        case "n":
                            break
                        case _:
                            print("\n\nSeleccione un valor valido")
                            continue

            #Lee el record
            case 2:
                with open("Record.txt", "a", encoding="UTF-8"):
                    pass
                with open("Record.txt", "r", encoding="UTF-8") as f:
                    for linea in f:
                        print(linea.strip())

            #Borra el record
            case 3:
                with open("Record.txt", "w", encoding="UTF-8") as f:
                    f.write("")

            #sale del ciclo
            case 4:
                break

            #Validacion de datos
            case _:
                print("\n\nSeleccione un valor correcto")
                continue


main()