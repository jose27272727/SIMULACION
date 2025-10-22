# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 09:45:51 2025

@author: JOSE
"""
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# === Funciones para generar distribuciones ===
def generar_distribucion(nombre, params, n=1000):
    if nombre == "Uniforme":
        a = int(params["a"].get())
        b = int(params["b"].get())
        data = np.random.randint(a, b + 1, n)
        titulo = f"UNIFORME DISCRETA (a={a}, b={b})"
    
    elif nombre == "Bernoulli":
        p = float(params["p"].get())
        data = np.random.binomial(1, p, n)
        titulo = f"BERNOULLI (p={p})"
    
    elif nombre == "Binomial":
        n_ensayos = int(params["n"].get())
        p = float(params["p"].get())
        data = np.random.binomial(n_ensayos, p, n)
        titulo = f"BINOMIAL (n={n_ensayos}, p={p})"
    
    elif nombre == "Poisson":
        lam = float(params["lam"].get())
        data = np.random.poisson(lam, n)
        titulo = f"POISSON (λ={lam})"
    
    else:
        data, titulo = np.array([]), ""
    
    return data, titulo


# === Crear parámetros dinámicos ===
def actualizar_parametros(event=None):
    for widget in frame_params.winfo_children():
        widget.destroy()

    distrib = combo.get()
    global parametros
    parametros = {}

    if distrib == "Uniforme":
        crear_parametro("a", "1", 0)
        crear_parametro("b", "6", 1)

    elif distrib == "Bernoulli":
        crear_parametro("p", "0.6", 0)

    elif distrib == "Binomial":
        crear_parametro("n", "10", 0)
        crear_parametro("p", "0.5", 1)

    elif distrib == "Poisson":
        crear_parametro("λ", "3", 0, key="lam")


def crear_parametro(nombre, valor, fila, key=None):
    k = key if key else nombre
    tk.Label(frame_params, text=f"{nombre}:", bg="#dff6ff", fg="#004b6b", font=("Arial", 11, "bold")).grid(row=fila, column=0, padx=10, pady=5, sticky="e")
    parametros[k] = tk.Entry(frame_params, width=10, font=("Arial", 11))
    parametros[k].insert(0, valor)
    parametros[k].grid(row=fila, column=1, padx=5, pady=5, sticky="w")


# === Graficar ===
def graficar():
    distrib = combo.get()
    data, titulo = generar_distribucion(distrib, parametros)
    if data.size == 0:
        return

    fig.clear()
    ax = fig.add_subplot(111)

    valores, conteo = np.unique(data, return_counts=True)
    ax.bar(valores, conteo, color='#0099cc', edgecolor='black', width=0.6)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frecuencia")
    ax.grid(True, linestyle='--', alpha=0.6)
    canvas.draw()


# === Ventana principal con scroll general ===
root = tk.Tk()
root.title("🎲 Simulador de Distribuciones Discretas")
root.geometry("850x650")

# === Contenedor con scroll ===
main_canvas = tk.Canvas(root, bg="#dff6ff", highlightthickness=0)
main_scroll = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
scroll_frame = tk.Frame(main_canvas, bg="#dff6ff")

scroll_frame.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
main_canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
main_canvas.configure(yscrollcommand=main_scroll.set)

main_canvas.pack(side="left", fill="both", expand=True)
main_scroll.pack(side="right", fill="y")


# === CABECERA ===
frame_top = tk.Frame(scroll_frame, bg="#62b6cb")
frame_top.pack(fill="x", pady=5)

tk.Label(frame_top, text="Simulador de Distribuciones Discretas",
         bg="#62b6cb", fg="white", font=("Segoe UI", 17, "bold")).pack(pady=10)

# === Selección ===
frame_select = tk.Frame(scroll_frame, bg="#dff6ff")
frame_select.pack(pady=10)

tk.Label(frame_select, text="Distribución:", bg="#dff6ff", fg="#004b6b", font=("Arial", 12, "bold")).pack(side="left", padx=5)
combo = ttk.Combobox(frame_select, values=["Uniforme", "Bernoulli", "Binomial", "Poisson"],
                     state="readonly", font=("Arial", 12), width=15)
combo.set("Uniforme")
combo.pack(side="left", padx=10)
combo.bind("<<ComboboxSelected>>", actualizar_parametros)

# === Parámetros ===
frame_params = tk.Frame(scroll_frame, bg="#dff6ff")
frame_params.pack(pady=10)
parametros = {}
actualizar_parametros()

# === Botón ===
def on_enter(e): e.widget.config(bg="#0078D7")
def on_leave(e): e.widget.config(bg="#0099cc")

boton = tk.Button(scroll_frame, text="🎨 Generar y Graficar", command=graficar,
                  bg="#0099cc", fg="white", font=("Segoe UI", 12, "bold"),
                  padx=15, pady=8, relief="flat", bd=0)
boton.pack(pady=10)
boton.bind("<Enter>", on_enter)
boton.bind("<Leave>", on_leave)

# === Gráfico ===
fig = plt.Figure(figsize=(7.5, 4.5), dpi=100, facecolor="#f9fbfc")
canvas = FigureCanvasTkAgg(fig, master=scroll_frame)
canvas.get_tk_widget().pack(padx=10, pady=10)

root.mainloop()
