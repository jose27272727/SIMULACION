# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 14:53:41 2025

@author: JOSE
"""
import tkinter as tk
from tkinter import ttk, messagebox
import random

class GameOfLifeRandom:
    def __init__(self, root, rows=20, cols=20, cell_size=25, init_prob=0.2):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.running = False
        self.init_prob = init_prob

        # Inicializar cuadrícula
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        # Canvas
        self.canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg="#d0ebff")
        self.canvas.pack()

        # Dibujar cuadrícula
        for i in range(rows):
            for j in range(cols):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

        # Click para encender/apagar celdas
        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Botones
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        self.start_btn = ttk.Button(frame, text="Iniciar simulación", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = ttk.Button(frame, text="Detener", command=self.stop)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.clear_btn = ttk.Button(frame, text="Limpiar", command=self.clear)
        self.clear_btn.grid(row=0, column=2, padx=5)

        self.reset_btn = ttk.Button(frame, text="Reiniciar", command=self.reset)
        self.reset_btn.grid(row=0, column=3, padx=5)

        self.randomize_grid()
        self.draw_grid()

    def randomize_grid(self):
        """Llena la cuadrícula con células vivas aleatorias"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = 1 if random.random() < self.init_prob else 0

    def toggle_cell(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 1 - self.grid[row][col]
            self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("cell")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    x1 = j * self.cell_size
                    y1 = i * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="cell")

    def start(self):
        if not self.running:
            self.running = True
            self.run()

    def stop(self):
        self.running = False

    def clear(self):
        self.running = False
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_grid()

    def reset(self):
        self.running = False
        self.randomize_grid()
        self.draw_grid()

    def run(self):
        if not self.running:
            return

        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        corner_hit = False

        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if alive_neighbors in [2,3]:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbors == 3:
                        new_grid[i][j] = 1

                # Verificar esquinas
                if new_grid[i][j] == 1 and ((i==0 and j==0) or (i==0 and j==self.cols-1) or
                                            (i==self.rows-1 and j==0) or (i==self.rows-1 and j==self.cols-1)):
                    corner_hit = True

        self.grid = new_grid
        self.draw_grid()

        if corner_hit:
            self.running = False
            if messagebox.askyesno("Esquina alcanzada", "¡Una célula llegó a la esquina!\n¿Desea reiniciar?"):
                self.reset()

        self.root.after(200, self.run)

    def count_neighbors(self, i, j):
        count = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x == 0 and y == 0:
                    continue
                ni, nj = i + x, j + y
                if 0 <= ni < self.rows and 0 <= nj < self.cols:
                    count += self.grid[ni][nj]
        return count

# --- Ejecución principal ---
root = tk.Tk()
root.title("Juego de la Vida Aleatorio")
app = GameOfLifeRandom(root)
root.mainloop()
