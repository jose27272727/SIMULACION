# -*- coding: utf-8 -*-
"""
Prueba de Uniformidad (Chi-Cuadrado) con tabla detallada
Guarda como: prueba_uniformidad_tabla.py
"""
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import chi2

def ejecutar_prueba():
    # leer entradas
    try:
        n = int(entry_n.get())
        k = int(entry_k.get())
        alpha = float(entry_alpha.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos (n, k, alpha).")
        return
    if n <= 0 or k <= 0:
        messagebox.showerror("Error", "n y k deben ser mayores que 0.")
        return
    if k > n:
        if not messagebox.askyesno("Atención", "k > n. ¿Desea continuar?"):
            return

    # generar Ri (si quieres usar tus propios valores, reemplaza esto)
    ri = np.random.rand(n)

    # obtener histogram (frecuencias)
    obs, edges = np.histogram(ri, bins=k, range=(0.0, 1.0))
    Ei = n / k

    # limpiar tabla
    for r in tree.get_children():
        tree.delete(r)

    # llenar tabla con intervalos y cálculos
    chi_sum = 0.0
    for i in range(k):
        a = edges[i]
        b = edges[i+1]
        intervalo = f"{a:.2f} - {b:.2f}"
        Oi = int(obs[i])
        contrib = ((Oi - Ei) ** 2) / Ei
        chi_sum += contrib
        tree.insert("", "end", values=(i+1, intervalo, Oi, f"{Ei:.2f}", f"{contrib:.4f}"))

    # fila total (sum)
    tree.insert("", "end", values=("", "Σ", "", "", f"{chi_sum:.4f}"))

    # chi crítico (tabla)
    df = k - 1
    chi_crit = chi2.ppf(1 - alpha, df=df)

    resultado = "✅ ACEPTA H0 (Uniformidad)" if chi_sum < chi_crit else "❌ RECHAZA H0"

    # mostrar resultados (texto)
    label_info.config(
        text=(f"n={n}   k={k}   α={alpha}   df={df}\n"
              f"Chi² calculado = {chi_sum:.4f}\n"
              f"Chi² crítico (1-α, df={df}) = {chi_crit:.4f}\n"
              f"Resultado: {resultado}")
    )

    # graficar histograma
    for w in graph_frame.winfo_children():
        w.destroy()
    fig, ax = plt.subplots(figsize=(5,3))
    ax.hist(ri, bins=edges, edgecolor="black", alpha=0.7)
    ax.set_title("Histograma de Ri")
    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")
    # dibujar línea de frecuencia esperada
    ax.axhline(Ei, color="red", linestyle="--", label=f"Ei = {Ei:.2f}")
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# ---------- Interfaz ----------
root = tk.Tk()
root.title("Prueba de Uniformidad - Tabla Chi²")
root.geometry("900x600")

top_frame = ttk.Frame(root, padding=8)
top_frame.pack(fill="x")

ttk.Label(top_frame, text="Cantidad n:").grid(row=0, column=0, sticky="w", padx=4)
entry_n = ttk.Entry(top_frame, width=10)
entry_n.insert(0, "100")
entry_n.grid(row=0, column=1, padx=4)

ttk.Label(top_frame, text="Intervalos k:").grid(row=0, column=2, sticky="w", padx=4)
entry_k = ttk.Entry(top_frame, width=10)
entry_k.insert(0, "10")
entry_k.grid(row=0, column=3, padx=4)

ttk.Label(top_frame, text="α (ej: 0.05):").grid(row=0, column=4, sticky="w", padx=4)
entry_alpha = ttk.Entry(top_frame, width=10)
entry_alpha.insert(0, "0.05")
entry_alpha.grid(row=0, column=5, padx=4)

btn_run = ttk.Button(top_frame, text="Ejecutar Prueba", command=ejecutar_prueba)
btn_run.grid(row=0, column=6, padx=10)

# content: tabla a la izquierda, gráfico a la derecha
content = ttk.Frame(root, padding=8)
content.pack(fill="both", expand=True)

# Tabla (Treeview) con scroll
table_frame = ttk.Frame(content)
table_frame.pack(side="left", fill="both", expand=True)

cols = ("#", "Intervalo", "Oi", "Ei", "((Oi-Ei)^2)/Ei")
tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=20)
for c in cols:
    tree.heading(c, text=c)
    if c == "Intervalo":
        tree.column(c, width=140, anchor="center")
    else:
        tree.column(c, width=90, anchor="center")
tree.pack(side="left", fill="both", expand=True)

vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")
tree.configure(yscrollcommand=vsb.set)

# Panel derecho: gráfico y resultados
right_frame = ttk.Frame(content)
right_frame.pack(side="right", fill="both", expand=True)

graph_frame = ttk.Frame(right_frame)
graph_frame.pack(fill="both", expand=True)

label_info = ttk.Label(right_frame, text="Resultados aparecerán aquí", font=("Arial", 10), padding=6)
label_info.pack(fill="x")

root.mainloop()
