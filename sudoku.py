from random import randint,choice

def one_list(lista):
    #Va a convertir listas anidadas en una sola lista
    final =[]
    for el in lista:
        if type(el)!=list:
            final.append(str(el))
        else:
            final.extend(one_list(el))
    return final


def generate_sudoku():
    sudoku = []
    #Este codigo crea lo basico del sudoku
    for i in range(9):
        possible = [i for i in range(1,10)]
        noveau = []
        for k in range(3):
            flie = []
            for m in range(3):
                if i%4==0:
                    x = choice(possible)
                    possible.remove(x)
                    flie.append(x)
                else:
                    flie.append(0)
            noveau.append(flie)
        sudoku.append(noveau)
    return sudoku


def filas(sudoku):
    #Va a devolvir una lista de las filas
    f_c = []
    for sec in range(3):
        sectores = sudoku[sec*3:(sec+1)*3]
        for bl in range(3):
            bloque = []
            for lin in range(3):
                bloque.append(sectores[lin][bl])
            f_c.append(one_list(bloque))
    return f_c

def columnas(sudoku):
    #Devuelve una Lista con las columnas
    col = []
    for su in range(3):
        for bloq in range(3):
            coli = []
            for lin in range(3):
                for sec in range(3):
                    coli.append(sudoku[lin*3+su][sec][bloq])
            col.append(one_list(coli))
    return col

def quitar_casillas(num,sudoku):
    cnt =0
    while cnt<num:
        bloq = randint(0,8)
        pos = randint(0,8)
        if sudoku[bloq][pos//3][pos%3]!=' ':
            sudoku[bloq][pos//3][pos%3] = ' '
            cnt+=1
    return sudoku


def llenar_bloque(idx,sudoku):
    #LLena el bloque dado
    bloque = [sudoku[idx][i] for i in range(3)]
    if bloque[0][0]!=0:
        return sudoku
    for fi in range(3):
        for cmn in range(3):
            fila = filas(sudoku)[fi+(idx//3)*3]
            columna = columnas(sudoku)[cmn+(idx%3)*3]
            bloq = one_list(bloque)
            azar = [str(i+1) for i in range(9)]
            for n in range(1,10):
                nu = choice(azar)
                if not(nu in columna) and not(nu in fila) and not(nu in bloq):
                    bloque[fi][cmn] = nu
                    break
                else:
                    azar.remove(nu)
    sudoku[idx] = bloque
    return sudoku
def mostrar_sudoku(filss):
    #Muestra el sudoku`
    fils2 = [filss[i] for i in range(len(filss))]
    fils =[fils2[i] for i in range(len(filss))]
    for linea in fils:
        linea.insert(3, '|')
        linea.insert(7, '|')
    cnt =0
    for fi in fils:
        cnt+=1
        print(' '.join(fi))
        if cnt%3==0 and cnt!=9:
            print('- - - | - - - | - - -')
    for linea in fils:
        linea.pop(7)
        linea.pop(3)
    

def paquete_sud(num):
    #Importante hay que convertir sudoku al final a filas :D
    num = num%81
    global sudoku
    sudoku = generate_sudoku()
    basic = [['0' for i in range(3)] for i in range(3)]
    cnt = 0
    while '0' in one_list(sudoku):
        sudoku = generate_sudoku()
        for bl in range(9):
            #Esto va a llenar los 9 bloques
            sudoku = llenar_bloque(bl,sudoku)
        continue
    original = filas(sudoku)
    sudoku = quitar_casillas(num,sudoku)
    mostrar_sudoku(filas(sudoku))
    return (original, sudoku)

def revisar_sudoku(filas,x,y,seleccion):
    #Va a revisar si la casilla marcada esta bien o no
    if filas[y-1][x-1]==str(seleccion):
        return True
    return False
def cambio_check(raw_sudoku,filas,x,y,seleccion):
    if (value:=revisar_sudoku(filas,x,y,seleccion)):
        raw_sudoku[y-1][x-1]= str(seleccion)
    final = True if not(' ' in one_list(raw_sudoku)) else False
    return raw_sudoku,(value),final


elec = int(input('Cuantas casillas quieres quitar?? => '))
paquete_sud(elec) #Genera el sudoku quitando tantas casillas deseadas