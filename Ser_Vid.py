from clases import *

#Creo los arrays
Series=[]
Video=[]

def Cuenta_Series():

    Series_entregadas = 0

    for ser in Series:
        if ser.Entregado==True:
            Series_entregadas= Series_entregadas +1
        else:
            Series_entregadas = Series_entregadas + 0

    print("Se han entregado " + str(Series_entregadas) +" series")

    #Devolvemos las series entregadas
    for dev in Series:
        if dev.Entregado==True:
            dev.devolver()

    com_ser=[]

    for com in Series:

        com_ser.append(com.get_Num_hyt())

    i=max(com_ser)


    for x in Series:
        if i == x.get_Num_hyt():
            print("La serie que mas temporadas tiene es " + str(x) + " temporadas. ")

def Cuenta_Video():

    Video_entregadas = 0

    for ser in Video:
        if ser.Entregado==True:
            Video_entregadas= Video_entregadas +1
        else:
            Video_entregadas = Video_entregadas + 0

    print("Se han entregado " + str(Video_entregadas) +" videojuegos")

    #Devolvemos las series entregadas
    for dev in Video:
        if dev.Entregado==True:
            dev.devolver()

    com_vid=[]

    for com in Video:

        com_vid.append(com.get_Num_hyt())

    i=max(com_vid)


    for x in Video:
        if i == x.get_Num_hyt():
            print("La serie que mas horas de juego tiene es " + str(x) + " horas. ")