import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

# Función para abrir cada script
def abrir_script(nombre_archivo):
    python = sys.executable  # Usa el mismo intérprete de Python
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
    subprocess.Popen([python, ruta])

# Ventana principal
root = tk.Tk()
root.title("Menú de Algoritmos de Generación y Pruebas")
root.geometry("450x400")
root.configure(bg="#f4f4f4")

ttk.Label(root, text="Seleccione un algoritmo o prueba", font=("Arial", 14, "bold")).pack(pady=20)

# Botones para los algoritmos
ttk.Button(root, text="Algoritmo de Cuadrados Medios", 
           command=lambda: abrir_script("cuadrados_medios.py")).pack(pady=10)

ttk.Button(root, text="Algoritmo de Productos Medios", 
           command=lambda: abrir_script("productos_medios.py")).pack(pady=10)

ttk.Button(root, text="Algoritmo de Multiplicador Constante", 
           command=lambda: abrir_script("multiplicador_constante.py")).pack(pady=10)

# Botones para las pruebas estadísticas
ttk.Button(root, text="Prueba de Medias", 
           command=lambda: abrir_script("prueba_medias.py")).pack(pady=10)

ttk.Button(root, text="Prueba de Varianza", 
           command=lambda: abrir_script("prueba_varianza.py")).pack(pady=10)

# Ejecutar
root.mainloop()
