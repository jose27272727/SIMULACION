# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 18:02:25 2025

@author: JOSE
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import norm

def generar_prueba_medias():
    n = int(entry_n.get())
    alpha = float(entry_alpha.get())
    
    # Generar números pseudoaleatorios uniformes [0,1]
    ri = np.random.rand(n)
    
    # Media esperada y desviación estándar para U(0,1)
    media_esperada = 0.5
    sigma = 1 / (12*n)**0.5  # std error de la media
    
    # Z crítico según la tabla Z
    z = norm.ppf(1 - alpha/2)
    
    # Límites
    li = media_esperada - z * sigma
    ls = media_esperada + z * sigma
    
    # Calcular media muestral
    media_muestral = np.mean(ri)
    
    # Mostrar resultados incluyendo Z
    label_resultado.config(
        text=f"Media muestral: {media_muestral:.4f}\n"
             f"Z (tabla Z): {z:.4f}\n"
             f"Límite inferior: {li:.4f}\n"
             f"Límite superior: {ls:.4f}"
    )
    
    # Graficar
    for widget in graph_frame.winfo_children():
        widget.destroy()
    
    fig, ax = plt.subplots(figsize=(5,4))
    ax.plot(ri, marker='o', linestyle='', label='Ri')
    ax.axhline(media_esperada, color='blue', label='Media esperada')
    ax.axhline(li, color='red', linestyle='--', label='Límite inferior')
    ax.axhline(ls, color='green', linestyle='--', label='Límite superior')
    ax.axhline(media_muestral, color='purple', linestyle='-', label='Media muestral')
    
    ax.set_title("Prueba de Medias")
    ax.set_xlabel("Iteración")
    ax.set_ylabel("Ri")
    ax.legend()
    
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("Prueba de Medias")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Cantidad de números (n):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(frame)
entry_n.grid(row=0, column=1)

tk.Label(frame, text="Nivel de significancia α (ej: 0.05):").grid(row=1, column=0, padx=5, pady=5)
entry_alpha = tk.Entry(frame)
entry_alpha.grid(row=1, column=1)

btn = tk.Button(frame, text="Generar Prueba", command=generar_prueba_medias)
btn.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(root, text="Resultados", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

graph_frame = tk.Frame(root, width=500, height=300, bg="white")
graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()

