
"""
Algoritmo de Cuadrados Medios (Middle-Square) con Tkinter
- Parámetros: semilla, dígitos, iteraciones
@author: JOSE
"""

import tkinter as tk
from tkinter import ttk, StringVar, IntVar, messagebox


def middle_square_sequence(seed: int, n_digits: int, iterations: int):
    x = int(str(seed).zfill(n_digits))
    width = 2 * n_digits
    registros = []

    for i in range(1, iterations + 1):
        x2 = x * x
        s = str(x2).zfill(width)
        ini = (len(s) - n_digits) // 2
        medio = s[ini:ini + n_digits]
        x_next = int(medio)
        u = x_next / (10 ** n_digits)

        registros.append({
            "i": i,
            "x": str(x).zfill(n_digits),
            "x2": s,
            "centro": medio,
            "u": u,
        })

        x = x_next

    return registros


class MiddleSquareApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algoritmo de Cuadrados Medios • Tkinter")
        self.geometry("800x600")
        self.minsize(700, 500)

        # Variables de control
        self.seed_var = StringVar(value="675248")
        self.n_digits_var = IntVar(value=6)
        self.iterations_var = IntVar(value=50)

        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, padding=10)
        container.pack(fill="both", expand=True)

        # Panel de controles
        controls = ttk.Labelframe(container, text="Parámetros", padding=10)
        controls.pack(fill="x")

        ttk.Label(controls, text="Semilla:").grid(row=0, column=0, sticky="w")
        seed_entry = ttk.Entry(controls, textvariable=self.seed_var, width=15)
        seed_entry.grid(row=0, column=1, padx=5)

        ttk.Label(controls, text="Dígitos (n):").grid(row=0, column=2, sticky="w")
        n_digits_spin = ttk.Spinbox(controls, from_=1, to=12, textvariable=self.n_digits_var, width=5)
        n_digits_spin.grid(row=0, column=3, padx=5)

        ttk.Label(controls, text="Iteraciones:").grid(row=0, column=4, sticky="w")
        iter_spin = ttk.Spinbox(controls, from_=1, to=10000, textvariable=self.iterations_var, width=7)
        iter_spin.grid(row=0, column=5, padx=5)

        gen_btn = ttk.Button(controls, text="Generar", command=self.generate_sequence)
        gen_btn.grid(row=0, column=6, padx=10)

        # Tabla con scroll
        table_frame = ttk.Labelframe(container, text="Secuencia generada", padding=8)
        table_frame.pack(fill="both", expand=True, pady=(10, 0))

        cols = ("i", "x", "x2", "centro", "u")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings")
        self.tree.pack(side="left", fill="both", expand=True)

        # Scroll vertical
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.heading("i", text="i")
        self.tree.heading("x", text="x")
        self.tree.heading("x2", text="x²")
        self.tree.heading("centro", text="Centro")
        self.tree.heading("u", text="u")

        for col in cols:
            self.tree.column(col, width=120, anchor="center")

    def generate_sequence(self):
        try:
            seed = int(self.seed_var.get())
            n_digits = int(self.n_digits_var.get())
            iterations = int(self.iterations_var.get())

            registros = middle_square_sequence(seed, n_digits, iterations)

            # Limpiar tabla
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Insertar filas
            for r in registros:
                self.tree.insert("", "end", values=(r["i"], r["x"], r["x2"], r["centro"], f"{r['u']:.6f}"))

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = MiddleSquareApp()
    app.mainloop()
