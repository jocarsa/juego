import tkinter as tk
ventana = tk.Tk()
ventana.geometry("500x500")
titulo = tk.Label(ventana,text = "Juego de Vicente",font=("Arial",25))
titulo.pack()
botonjugar = tk.Button(text="Jugar")
botonjugar.pack()
