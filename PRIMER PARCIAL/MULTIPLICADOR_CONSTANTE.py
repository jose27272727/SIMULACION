# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 17:44:07 2025

@author: JOSE
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def multiplicador_constante(semilla, constante, iteraciones):
    resultados = []
    x = semilla
    for i in range(iteraciones):
        multiplicacion = x * constante  # resultado de la multiplicación
        s = str(multiplicacion).zfill(8)  # asegurar longitud mínima
        mitad = len(s) // 2
        x = int(s[mitad-2:mitad+2])  # tomar 4 dígitos centrales
        r = x / 10000
        resultados.append((i+1, multiplicacion, x, r))
    return resultados

def generar():
    semilla = int(entry_semilla.get())
    constante = int(entry_constante.get())
    n = int(entry_iteraciones.get())

    datos = multiplicador_constante(semilla, constante, n)

    # limpiar tabla
    for row in tree.get_children():
        tree.delete(row)

    # insertar datos
    for fila in datos:
        tree.insert("", tk.END, values=fila)

    # calcular promedio de Ri
    promedio = sum(r[3] for r in datos) / len(datos)
    label_promedio.config(text=f"Promedio de Ri: {promedio:.4f}")

    # limpiar gráfico anterior si existe
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # crear nueva figura
    fig, ax = plt.subplots(figsize=(5,4))
    ax.plot([r[3] for r in datos], marker='o')
    ax.set_title("Generador por Multiplicador Constante")
    ax.set_xlabel("Iteración")
    ax.set_ylabel("Ri")

    # incrustar gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Interfaz Tkinter
root = tk.Tk()
root.title("Algoritmo Multiplicador Constante")

# ---- Entradas ----
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Semilla:").grid(row=0, column=0, padx=5, pady=5)
entry_semilla = tk.Entry(frame)
entry_semilla.grid(row=0, column=1)

tk.Label(frame, text="Constante:").grid(row=1, column=0, padx=5, pady=5)
entry_constante = tk.Entry(frame)
entry_constante.grid(row=1, column=1)

tk.Label(frame, text="Iteraciones:").grid(row=2, column=0, padx=5, pady=5)
entry_iteraciones = tk.Entry(frame)
entry_iteraciones.grid(row=2, column=1)

btn = tk.Button(frame, text="Generar", command=generar)
btn.grid(row=3, column=0, columnspan=2, pady=10)

# ---- Contenedor tabla + gráfico ----
content_frame = tk.Frame(root)
content_frame.pack(pady=10, fill="both", expand=True)

# ---- Tabla con scroll ----
table_frame = tk.Frame(content_frame)
table_frame.pack(side="left", fill="both", expand=True)

columns = ("Iteración", "Multiplicación", "Valor Central", "Ri")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ---- Gráfico incrustado ----
graph_frame = tk.Frame(content_frame, width=400, height=300, bg="white")
graph_frame.pack(side="right", fill="both", expand=True)

# ---- Promedio de Ri ----
label_promedio = tk.Label(root, text="Promedio de Ri: -", font=("Arial", 12, "bold"))
label_promedio.pack(pady=10)

root.mainloop()



