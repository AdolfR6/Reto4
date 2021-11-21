from clases import *
from Ser_Vid import *

#Creo los 5 objetos Serie y los introduzco en el array Series
ser1=Serie("Simpsons","Comedia","Matt Groening",31)
Series.append(ser1)
ser2=Serie("Soprano","Mafia","David Chase",6)
Series.append(ser2)
ser3=Serie("Narcos","Comedia","Chris Brancato",3)
Series.append(ser3)
ser4=Serie("Startrek Entreprise","Ciencia-Ficcion","Gene Roddenberry",4)
Series.append(ser4)
ser5=Serie("Pade de familia","Comedia","Seth MacFarlane",20)
Series.append(ser5)

#Entrego varias series
ser1.entregar()
ser4.entregar()
ser2.entregar()

Cuenta_Series()

#Creo los 5 objetos Videojuego y los introduzco en el array Videojuegos
vid1=Videojuego("Gran Turismo","Simulador","Polyphony Digital",200)
Video.append(vid1)
vid2=Videojuego("FiFA 21","Futbol","EA Sports",500)
Video.append(vid2)
vid3=Videojuego("God of War","Acción","SCE Santa Monica Studio",600)
Video.append(vid3)
vid4=Videojuego("Warcraft","Estrategia","Blizzard Entertainment",150)
Video.append(vid4)
vid5=Videojuego("Mario Bros","Plataforma","Nintendo",175)
Video.append(vid5)


#Entrego varias videojuegos
vid1.entregar()
vid3.entregar()

Cuenta_Video()