import tkinter as tk
##from PIL import ImageTk, Image

def mostrar_interfaz(imagen):
    # Crear la ventana principal
    ventana = tk.Tk()

    # Configurar el tamaño de la ventana
    ventana.geometry("600x500")

    # Título y descripción
    titulo = tk.Label(ventana, text="Título", font=("Arial", 18))
    titulo.pack(pady=10)

    descripcion = tk.Label(ventana, text="Descripción de un párrafo", font=("Arial", 12), wraplength=500)
    descripcion.pack(pady=10)

    # Cargar la imagen
    # imagen_path = Image.open(imagen)
    # imagen_resized = imagen_path.resize((600, 300), Image.ANTIALIAS)
    # imagen_tk = ImageTk.PhotoImage(imagen_resized)
    # imagen_label = tk.Label(ventana, image=imagen_tk)
    # imagen_label.pack(pady=10)

    # Input de texto centrado
    input_texto = tk.Entry(ventana, width=50, justify="center")
    input_texto.pack(pady=10)

    # Botones
    boton1 = tk.Button(ventana, text="Mostrar Imagen 1", command=lambda: mostrar_interfaz("imagen1.png"))
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Mostrar Imagen 2", command=lambda: mostrar_interfaz("imagen2.png"))
    boton2.pack(pady=10)

    # Mostrar la interfaz
    ventana.mainloop()

# Iniciar la interfaz con la primera imagen
mostrar_interfaz("imagen1.png")