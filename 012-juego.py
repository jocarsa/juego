print("Juego de Vicente")
#importamos librería para hacer ventanas
import tkinter as tk
#creamos una ventana
ventana = tk.Tk()
#tamaño de la ventana
ventana.geometry("500x500")
#insertamos una imagen
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
    posy = posy - 0.01
    pegatina.place(relx = posx,rely = posy,anchor = "center")
    
