# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 09:40:58 2025

@author: JOSE
"""
import tkinter as tk
from tkinter import ttk, messagebox
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generar():
    try:
        dist = combo_tipo.get()
        cantidad = int(entry_cant.get())
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor que cero.")
            return

        valores = []

        # --- UNIFORME ---
        if dist == "Uniforme":
            a = float(entry_param1.get())
            b = float(entry_param2.get())
            if a >= b:
                messagebox.showerror("Error", "El mínimo debe ser menor que el máximo.")
                return
            valores = [round(random.uniform(a, b), 2) for _ in range(cantidad)]

        # --- K-ERLANG ---
        elif dist == "k-Erlang":
            k = float(entry_param1.get())
            theta = float(entry_param2.get())
            valores = [round(random.gammavariate(k, theta / k), 2) for _ in range(cantidad)]

        # --- EXPONENCIAL ---
        elif dist == "Exponencial":
            lambd = float(entry_param1.get())
            valores = [round(random.gammavariate(1, lambd), 2) for _ in range(cantidad)]

        # --- GAMMA ---
        elif dist == "Gamma":
            media = float(entry_param1.get())
            varianza = float(entry_param2.get())
            forma = (media ** 2) / varianza
            escala = varianza / media
            valores = [round(random.gammavariate(forma, escala), 2) for _ in range(cantidad)]

        # --- NORMAL ---
        elif dist == "Normal":
            media = float(entry_param1.get())
            varianza = float(entry_param2.get())
            valores = [round(random.normalvariate(media, np.sqrt(varianza)), 2) for _ in range(cantidad)]

        # --- WEIBULL ---
        elif dist == "Weibull":
            forma = float(entry_param1.get())
            escala = float(entry_param2.get())
            desplaz = float(entry_param3.get()) if entry_param3.get() != "" else 0
            valores = [round(desplaz + (escala ** 2) * ((-np.log(1 - random.random())) ** (1 / forma)), 2)
                       for _ in range(cantidad)]

        # Limpiar tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Insertar nuevos valores
        for i, v in enumerate(valores, start=1):
            tabla.insert("", "end", values=(i, v))

        # Mostrar gráfico
        mostrar_grafico(valores, dist)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")


def mostrar_grafico(valores, titulo):
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(8, 4))
    n, bins, patches = ax.hist(valores, bins=10, color="#5DADE2", edgecolor="black", rwidth=0.9)

    for i in range(len(n)):
        ax.text(bins[i] + (bins[i + 1] - bins[i]) / 2, n[i] + 0.3, str(int(n[i])),
                ha='center', va='bottom', fontsize=8)

    ax.set_title(f"Distribución {titulo}", fontsize=13, weight="bold")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frecuencia")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def actualizar_campos(event=None):
    dist = combo_tipo.get()
    for w in [lbl_p1, lbl_p2, lbl_p3, entry_param1, entry_param2, entry_param3]:
        w.pack_forget()

    if dist == "Uniforme":
        lbl_p1.config(text="Mínimo (a):"); lbl_p2.config(text="Máximo (b):")
        lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack()

    elif dist == "k-Erlang":
        lbl_p1.config(text="Forma (k):"); lbl_p2.config(text="Escala (θ):")
        lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack()

    elif dist == "Exponencial":
        lbl_p1.config(text="Escala (λ):")
        lbl_p1.pack(); entry_param1.pack()

    elif dist == "Gamma":
        lbl_p1.config(text="Media (μ):"); lbl_p2.config(text="Varianza (σ²):")
        lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack()

    elif dist == "Normal":
        lbl_p1.config(text="Media (μ):"); lbl_p2.config(text="Varianza (σ²):")
        lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack()

    elif dist == "Weibull":
        lbl_p1.config(text="Forma (β):"); lbl_p2.config(text="Escala (η):"); lbl_p3.config(text="Desplazamiento (opcional):")
        lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack(); lbl_p3.pack(); entry_param3.pack()


# ---------------- INTERFAZ PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("Simulador de Distribuciones")
ventana.state('zoomed')  # Pantalla completa
ventana.configure(bg="#f5f6fa")

# --- Canvas con scrollbar global ---
canvas = tk.Canvas(ventana, bg="#f5f6fa")
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Frame dentro del Canvas (donde irá todo el contenido)
contenedor = tk.Frame(canvas, bg="#f5f6fa")
canvas.create_window((0, 0), window=contenedor, anchor="nw")

# Ajuste del scroll cuando cambia el tamaño
def configurar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
contenedor.bind("<Configure>", configurar_scroll)

# Permitir scroll con la rueda del mouse
def scroll_mouse(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
canvas.bind_all("<MouseWheel>", scroll_mouse)

# ---------------- CONTENIDO ----------------
frame_superior = tk.Frame(contenedor, bg="#f5f6fa")
frame_superior.pack(pady=15)

tk.Label(frame_superior, text="Tipo de Distribución:", bg="#f5f6fa", font=("Arial", 12, "bold")).pack(pady=5)
combo_tipo = ttk.Combobox(frame_superior, values=["Uniforme", "k-Erlang", "Exponencial", "Gamma", "Normal", "Weibull"], width=25)
combo_tipo.current(0)
combo_tipo.pack()
combo_tipo.bind("<<ComboboxSelected>>", actualizar_campos)

lbl_p1 = tk.Label(frame_superior, text="Mínimo (a):", bg="#f5f6fa")
entry_param1 = tk.Entry(frame_superior)
lbl_p2 = tk.Label(frame_superior, text="Máximo (b):", bg="#f5f6fa")
entry_param2 = tk.Entry(frame_superior)
lbl_p3 = tk.Label(frame_superior, text="Desplazamiento:", bg="#f5f6fa")
entry_param3 = tk.Entry(frame_superior)

lbl_p1.pack(); entry_param1.pack(); lbl_p2.pack(); entry_param2.pack()

tk.Label(frame_superior, text="Cantidad de valores:", bg="#f5f6fa", font=("Arial", 12, "bold")).pack(pady=5)
entry_cant = tk.Entry(frame_superior)
entry_cant.pack()

tk.Button(frame_superior, text="Generar", command=generar, bg="#27ae60", fg="white",
          font=('Arial', 11, 'bold'), padx=10, pady=5).pack(pady=10)

# --- Tabla con scroll ---
frame_tabla = tk.Frame(contenedor)
frame_tabla.pack(pady=15, fill="x")

scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
scroll_x = ttk.Scrollbar(frame_tabla, orient="horizontal")

tabla = ttk.Treeview(frame_tabla, columns=("N°", "Valor"), show="headings",
                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, height=15)
scroll_y.config(command=tabla.yview)
scroll_x.config(command=tabla.xview)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tabla.pack(fill="both", expand=True)

tabla.heading("N°", text="N°")
tabla.heading("Valor", text="Valor")
tabla.column("N°", width=80, anchor="center")
tabla.column("Valor", width=120, anchor="center")

# --- Gráfico ---
frame_grafico = tk.Frame(contenedor, bg="white", bd=2, relief="groove")
frame_grafico.pack(fill="both", expand=True, padx=15, pady=10)

ventana.mainloop()
