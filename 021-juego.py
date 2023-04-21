print("Juego de Vicente")
#importamos librería para hacer ventanas
import tkinter as tk
#creamos una ventana
ventana = tk.Tk()
#tamaño de la ventana
ventana.geometry("500x500")
#insertamos una imagen
#https://jocarsa.com/go/juego/personaje.png

mapa = tk.PhotoImage(file="mapa.png")
pegatinamapa = tk.Label(ventana, image=mapa)
pegatinamapa.place(relx = 0.5,rely = 0.5,anchor = "center")

personaje = tk.PhotoImage(file="personaje.png")

#Insertamos una etiqueta
pegatina = tk.Label(ventana, image=personaje)
#Mostramos la imagen
pegatina.place(relx = 0.5,rely = 0.5,anchor = "center")
#coordenadas del personaje
posx = 0.5
posy = 0.5
#vamos a mover el personaje
ventana.bind("<w>", lambda x: arriba())
def arriba():
    print("movemos el personaje hacia arriba")
    global posy
    if posy > 0:
        posy = posy - 0.01
    pegatina.place(relx = posx,rely = posy,anchor = "center")
ventana.bind("<s>", lambda x: abajo())
def abajo():
    print("movemos el personaje hacia abajo")
    global posy
    if posy < 0.9:
        posy = posy + 0.01  
    pegatina.place(relx = posx,rely = posy,anchor = "center")
ventana.bind("<a>", lambda x: izquierda())
def izquierda():
    print("movemos el personaje hacia la izquierda")
    global posx
    if posx > 0.1:
        posx = posx - 0.01
    pegatina.place(relx = posx,rely = posy,anchor = "center")
ventana.bind("<d>", lambda x: derecha())
def derecha():
    print("movemos el personaje hacia la derecha")
    global posx
    if posx < 0.9:
        posx = posx + 0.01
    pegatina.place(relx = posx,rely = posy,anchor = "center")
    
