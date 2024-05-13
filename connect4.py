from operator import truediv
from os import system
import turtle
from pkg_resources import VersionConflict
xTablero = 0
tablero = turtle.Turtle()
tablero.ht()
circulo = turtle.Turtle()
circulo.ht()
victoria = False
empate = False
def crear():
    #CONTORNO
    tablero.width(10)
    tablero.speed(500)
    tablero.penup()
    tablero.goto(-350,300)
    tablero.pendown()
    tablero.forward(700)
    tablero.right(90)
    tablero.forward(600)
    tablero.right(90)
    tablero.forward(700)
    tablero.right(90)
    tablero.forward(600)
    
    #VERTICAL
    xTablero = -250
    tablero.penup()
    tablero.goto(xTablero,300)
    tablero.pendown()
    tablero.right(180)
    for i in range(6):
        tablero.forward(600)
        tablero.penup()
        xTablero += 100
        tablero.goto(xTablero,300)
        tablero.pendown()
    xTablero = 0
    tablero.penup()
        
    #HORIZONTAL
    xTablero = 200
    tablero.goto(-350,xTablero)
    tablero.pendown()
    tablero.left(90)
    for i in range(5):
        tablero.forward(700)
        xTablero -= 100
        tablero.penup()
        tablero.goto(-350,xTablero)
        tablero.pendown()
    tablero.penup()
    
    xTablero = -320
    #NUMEROS
    for i in range(7):
        tablero.goto(xTablero,320)
        tablero.write(i+1,move=False, font=("arial",20))
        xTablero += 100
        
def ficha(x,y,c):
    #SETTINGS DE FICHA
    circulo.color("black")
    circulo.width(5)
    circulo.speed(500)
    circulo.penup()
    #POSICION
    circulo.goto(x,y)
    circulo.pendown()
    #DIBUJAR Y PINTAR
    circulo.begin_fill()
    circulo.circle(50)
    circulo.color(c)
    circulo.end_fill()
    ganaRojo()
    ganaAma()
coordenadasX = {
    1: -300,
    2: -200,
    3: -100,
    4: 0,
    5: 100,
    6: 200,
    7: 300
}
coordenadasY = {
    6: 200,
    5: 100,
    4: 0,
    3: -100,
    2: -200,
    1: -300,
}
espaciosY = [0,0,0,0,0,0,0,0]
##ROJO
rojoPosX = []
rojoPosY = []
##AMARILLO
amaPosX = []
amaPosY =[]
msg = "INGRESE LA COLUMNA \n(NO SE TOMARAN EN CUENTA LOS DECIMALES)"
def turnoRojo(msg):
    #CREAR INPUT BOX
    ws = turtle.Screen()
    ws.setup(900,700)
    #PEDIR VALOR X
    x = int(turtle.numinput("TURNO ROJO",msg,minval=1,maxval=7))
    if espaciosY[x] < 6:
        #print(espaciosY[x])
        rojoPosX.append(x)
        ##DETERMINAR Y
        nuevaPos = espaciosY[x]+1
        rojoPosY.append(nuevaPos)
        espaciosY[x] += 1
        ##NUEVAS VARIABLES
        x = coordenadasX[x]
        #print("Pos X fijada: " + str(x))
        y = coordenadasY[nuevaPos]
        #print("Pos Y fijada: " + str(y))
        c = "Red"
        ficha(x,y,c)
        x = 0
        y= 0
        msg = "INGRESE LA COLUMNA \n(NO SE TOMARAN EN CUENTA LOS DECIMALES)"
    else:
        msg = "YA NO SE PUEDE COLOCAR PIEZAS EN ESTA COLUMNA\nINGRESE OTRA COLUMNA"
        cont = 0
        for i in range(7):
            if espaciosY[i+1] == 6:
                cont += 1
        if cont == 7:
            print("TABLERO LLENO \n EMPATE")
            turtle.textinput("Mensaje","TABLERO LLENO \n EMPATE \nPresiona 'OK' para continuar")
            menu()
        else:
            print("CONTINUAR")
            turnoRojo(msg)
def turnoAma (msg):
    #CREAR INPUT BOX
    ws = turtle.Screen()
    ws.setup(900,700)
    #PEDIR VALOR X
    x = int(turtle.numinput("TURNO AMA",msg,minval=1,maxval=7))
    if espaciosY[x] < 6:
        #print(espaciosY[x])
        amaPosX.append(x)
        ##DETERMINAR Y
        nuevaPos = espaciosY[x]+1
        amaPosY.append(nuevaPos)
        espaciosY[x] += 1
        ##NUEVAS VARIABLES
        x = coordenadasX[x]
        #print("Pos X fijada: " + str(x))
        y = coordenadasY[nuevaPos]
        #print("Pos Y fijada: " + str(y))
        c = "Yellow"
        ficha(x,y,c)
        x = 0
        y= 0
        msg = "INGRESE LA COLUMNA \n(NO SE TOMARAN EN CUENTA LOS DECIMALES)"
    else:
        msg = "YA NO SE PUEDE COLOCAR PIEZAS EN ESTA COLUMNA\nINGRESE OTRA COLUMNA"
        cont = 0
        for i in range(7):
            if espaciosY[i+1] == 6:
                cont += 1
        if cont == 7:
            print("TABLERO LLENO \n EMPATE")
            turtle.textinput("Mensaje","TABLERO LLENO \n EMPATE \nPresiona 'OK' para continuar")
            menu()
        else:
            print("CONTINUAR")
            turnoAma(msg)
def ganaRojo():
    #HORIZONTAL
    cantFilaRojo = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }
    cont = 0
    for i in range(len(rojoPosY)):
        cantFilaRojo[rojoPosY[i]].append(rojoPosX[i])
        #print(cantFilaRojo)
    for i in range(len(cantFilaRojo)):
        #VERIFICA QUE HAYAN 4 O MAS EN LA MISMA FILA
        if len(cantFilaRojo[i+1]) >= 4:
            #print("mas de 4 en "+str(i+1))
            #verifica si estan al lado
            cantFilaRojo[i+1].sort()
            #print(cantFilaRojo[i+1])
            for j in range(len(cantFilaRojo[i+1])-1):
                #print("VERIFICANDO SI GANA"+str(i))
                if (cantFilaRojo[i+1][j]) == (cantFilaRojo[i+1][j+1])-1:
                    cont += 1
                   #print(cont)
                    if cont == 3:
                        print("gana HORIZONTAL ROJO")
                        turtle.textinput("Mensaje","gana HORIZONTAL ROJO \nPresiona 'OK' para continuar")
                        menu()
                        break  
                else:
                    cont = 0
    #VERTICAL
    cont = 0
    cantColRojo = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    #print('LLENAR "CantColRojo()"')
    for i in range(len(rojoPosX)):
        cantColRojo[rojoPosX[i]].append(rojoPosY[i])
        #print(cantColRojo)
        #VERIFICAR SI HAY 4 O MAS EN LA COLUMNA
    for i in range(len(cantColRojo)):
        if len(cantColRojo[i+1]) >= 4:
            #print("mas de 4 en "+str(i+1))
            #verifica si estan encima de otra
            cantColRojo[i+1].sort()
            #print(cantFilaRojo[i+1])
            for j in range(len(cantColRojo[i+1])-1):
                #print("VERIFICANDO SI GANA "+str(i))
                if (cantColRojo[i+1][j]) == (cantColRojo[i+1][j+1])-1:
                    cont += 1
                    #print(cont)
                    if cont == 3:
                        print("gana VERTICAL ROJO")
                        turtle.textinput("Mensaje","gana VERTICAL ROJO \nPresiona 'OK' para continuar")
                        menu()
                        break  
                else:
                    cont = 0
##TURNO AMARILLO
def ganaAma():
    #HORIZONTAL
    cantFilaAma = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }
    cont = 0
    for i in range(len(amaPosY)):
        cantFilaAma[amaPosY[i]].append(amaPosX[i])
        #print(cantFilaAma)
    for i in range(len(cantFilaAma)):
        #VERIFICA QUE HAYAN 4 O MAS EN LA MISMA FILA
        if len(cantFilaAma[i+1]) >= 4:
            #print("mas de 4 en "+str(i+1))
            #verifica si estan al lado
            cantFilaAma[i+1].sort()
            #print(cantFilaAma[i+1])
            for j in range(len(cantFilaAma[i+1])-1):
                #print("VERIFICANDO SI GANA"+str(i))
                if (cantFilaAma[i+1][j]) == (cantFilaAma[i+1][j+1])-1:
                    cont += 1
                   #print(cont)
                    if cont == 3:
                        print("gana HORIZONTAL AMARILLO")
                        turtle.textinput("Mensaje","gana HORIZONTAL AMARILLO \nPresiona 'OK' para continuar")
                        menu()
                        break  
                else:
                    cont = 0
    #VERTICAL
    cont = 0
    cantColAma = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    #print('LLENAR "CantColAma()"')
    for i in range(len(amaPosX)):
        cantColAma[amaPosX[i]].append(amaPosY[i])
        #print(cantColAma)
        #VERIFICAR SI HAY 4 O MAS EN LA COLUMNA
    for i in range(len(cantColAma)):
        if len(cantColAma[i+1]) >= 4:
            #print("mas de 4 en "+str(i+1))
            #verifica si estan encima de otra
            cantColAma[i+1].sort()
            #print(cantFilaAma[i+1])
            for j in range(len(cantColAma[i+1])-1):
                #print("VERIFICANDO SI GANA "+str(i))
                if (cantColAma[i+1][j]) == (cantColAma[i+1][j+1])-1:
                    cont += 1
                    #print(cont)
                    if cont == 3:
                        print("gana VERTICAL AMARILLO")
                        turtle.textinput("Mensaje","gana VERTICAL AMARILLO \nPresiona 'OK' para continuar")
                        menu()
                        break  
                else:
                    cont = 0
def menu():
    ws = turtle.Screen()
    ws.setup(900,700)
    #PEDIR OPCION MENU
    opcion = int(turtle.numinput("DEREK ARREAGA","-------BIENVENIDO A CONECTA 4-------\n--------INGRESE 1 PARA JUGAR--------\n--------INGRESE 2 PARA SALIR--------",minval=1,maxval=2))
    crear()
    if opcion == 1:
        victoria = False
        empate = False
        for i in range(42):
            turnoRojo(msg)
            turnoAma(msg)
    elif opcion == 2:
        raise SystemExit 
    
menu()
          
turtle.done()