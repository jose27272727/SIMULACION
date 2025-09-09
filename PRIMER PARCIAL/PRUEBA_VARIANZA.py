# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 16:29:10 2025

@author: JOSE
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import chi2

def generar_prueba_varianza():
    try:
        n = int(entry_n.get())
        alpha = float(entry_alpha.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")
        return

    # Generar números pseudoaleatorios [0,1]
    ri = np.random.rand(n)

    # Varianza muestral
    s2 = np.var(ri, ddof=1)

    # Varianza teórica de U(0,1)
    sigma2 = 1/12

    # Estadístico Chi-cuadrado
    chi_calc = (n-1) * s2 / sigma2

    # Límites del intervalo
    chi_inf = chi2.ppf(alpha/2, df=n-1)
    chi_sup = chi2.ppf(1 - alpha/2, df=n-1)

    # Evaluación
    resultado = "✅ ACEPTA H0 (varianza consistente)" if chi_inf < chi_calc < chi_sup else "❌ RECHAZA H0"

    # Mostrar resultados
    label_resultado.config(
        text=f"Varianza muestral: {s2:.5f}\n"
             f"Chi² calculado: {chi_calc:.4f}\n"
             f"Límite inferior: {chi_inf:.4f}\n"
             f"Límite superior: {chi_sup:.4f}\n"
             f"Resultado: {resultado}"
    )

    # Graficar histograma de los Ri
    for widget in graph_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(5,4))
    ax.hist(ri, bins=10, edgecolor="black", alpha=0.7)
    ax.set_title("Histograma de Ri")
    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("Prueba de Varianza")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Cantidad de números (n):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(frame)
entry_n.grid(row=0, column=1)

tk.Label(frame, text="Nivel de significancia α (ej: 0.05):").grid(row=1, column=0, padx=5, pady=5)
entry_alpha = tk.Entry(frame)
entry_alpha.grid(row=1, column=1)

btn = tk.Button(frame, text="Generar Prueba", command=generar_prueba_varianza)
btn.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(root, text="Resultados", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

graph_frame = tk.Frame(root, width=500, height=300, bg="white")
graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
