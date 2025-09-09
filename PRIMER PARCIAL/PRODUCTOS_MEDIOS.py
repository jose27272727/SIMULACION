# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 17:35:41 2025

@author: JOSE
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def productos_medios(x0, x1, n, d):
    resultados = []
    for i in range(n):
        producto = x0 * x1
        p_str = str(producto).zfill(2*d)  # rellenar con ceros
        inicio = (len(p_str) - d) // 2
        centro = int(p_str[inicio:inicio+d])
        ri = centro / (10**d)
        resultados.append((i+1, x0, x1, producto, centro, ri))
        x0, x1 = x1, centro
    return resultados

def generar():
    try:
        x0 = int(entry_x0.get())
        x1 = int(entry_x1.get())
        n = int(entry_n.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
        return

    d = len(str(x0))  # cantidad de dígitos de la semilla
    datos = productos_medios(x0, x1, n, d)

    # limpiar tabla
    for row in tabla.get_children():
        tabla.delete(row)

    # insertar datos
    for fila in datos:
        tabla.insert("", tk.END, values=fila)

    # Calcular estadísticas
    numeros = [fila[5] for fila in datos]
    media = np.mean(numeros)
    varianza = np.var(numeros)
    minimo = np.min(numeros)
    maximo = np.max(numeros)

    lbl_stats.config(
        text=f"Media: {media:.4f} | Varianza: {varianza:.4f} | "
             f"Mín: {minimo:.4f} | Máx: {maximo:.4f}"
    )

    # Actualizar gráfico
    mostrar_grafico(numeros)

def mostrar_grafico(numeros):
    # limpiar gráfico previo
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(5,3))
    ax.hist(numeros, bins=10, edgecolor='black', alpha=0.7)
    ax.set_title("Histograma de números Ri")
    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Interfaz
root = tk.Tk()
root.title("Algoritmo de Productos Medios")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Semilla X0:").grid(row=0, column=0)
entry_x0 = tk.Entry(frame)
entry_x0.grid(row=0, column=1)

tk.Label(frame, text="Semilla X1:").grid(row=1, column=0)
entry_x1 = tk.Entry(frame)
entry_x1.grid(row=1, column=1)

tk.Label(frame, text="Iteraciones:").grid(row=2, column=0)
entry_n = tk.Entry(frame)
entry_n.grid(row=2, column=1)

tk.Button(frame, text="Generar", command=generar).grid(row=3, column=0, columnspan=2, pady=5)

# Tabla con scroll
cols = ("i", "X0", "X1", "Producto", "Centro", "Ri")
tabla = ttk.Treeview(root, columns=cols, show="headings", height=15)

for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=100)

scroll_y = ttk.Scrollbar(root, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scroll_y.set)

tabla.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Estadísticas
lbl_stats = tk.Label(root, text="Media: - | Varianza: - | Mín: - | Máx: -", font=("Arial", 10))
lbl_stats.pack(pady=10)

# Frame para gráfico
frame_grafico = tk.Frame(root, bd=2, relief="sunken")
frame_grafico.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()

