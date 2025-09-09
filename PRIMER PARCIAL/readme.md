# CUADRADOS MEDIOS

# Algoritmo de Cuadrados Medios (Middle-Square) con Tkinter

Este proyecto implementa el **método de Cuadrados Medios** para generar números pseudoaleatorios con una interfaz gráfica usando **Tkinter** en Python.

## Características

- Interfaz gráfica simple con Tkinter.
- Parámetros configurables:
  - Semilla inicial (entero ≥ 0)
  - Número de dígitos (n)
  - Número de iteraciones (exactamente las indicadas)
- Tabla dinámica para mostrar la secuencia generada.
- Scroll vertical para navegar cuando hay muchas iteraciones.

## Requisitos

- Python 3.x
- Tkinter (estándar en Python)

## Cómo ejecutar

1. Clonar o descargar el proyecto.
2. Ejecutar el script:

```bash
python middle_square_gui.py


## Productos medios
Este programa genera números pseudoaleatorios con el **algoritmo de productos medios** usando Tkinter para la interfaz.


1. Se eligen dos semillas `X0` y `X1`.
2. Se multiplica: `P = X0 * X1`.
3. Se toman los dígitos centrales del producto.
4. Ese valor es el nuevo número y se repite el proceso.


- Muestra los resultados en una tabla con scroll.
- Calcula estadísticas: media, varianza, mínimo y máximo.
- Dibuja un histograma de los números generados dentro de la interfaz.


- Python 3
- Librerías: `tkinter`, `numpy`, `matplotlib`

Instalar dependencias:
```bash
pip install numpy matplotlib


# Algoritmo Multiplicador Constante - Python

Este programa genera números pseudoaleatorios usando el método del **multiplicador constante** y los muestra en una interfaz gráfica con **Tkinter**.


- Entrada de **semilla**, **constante** e **iteraciones**.  
- Tabla con iteración, resultado de la multiplicación, valor central y número pseudoaleatorio Ri.  
- Gráfico al lado de la tabla mostrando la evolución de Ri.  
- Cálculo y visualización del **promedio de Ri**.  
- Scroll vertical para manejar muchas iteraciones.

## Requisitos
- Python 3.x  
- Librerías: `tkinter`, `matplotlib`, `numpy`

## Uso
1. Ejecuta el archivo `multiplicador_constante.py`.  
2. Ingresa **semilla**, **constante** e **iteraciones**.  
3. Presiona **Generar**.  
4. Observa la tabla, el gráfico y el promedio de Ri.


# Prueba de Medias - Python

Este programa realiza la **prueba de medias** para números pseudoaleatorios generados uniformemente entre 0 y 1.

## Características
- Genera números aleatorios (`Ri`) y calcula su **media muestral**.  
- Calcula **límites inferior y superior** usando la **tabla Z** según un nivel de significancia α.  
- Muestra un **gráfico** con los números Ri, la media esperada, la media muestral y los límites.  
- Interfaz con **Tkinter** y gráficos incrustados con **Matplotlib**.

## Requisitos
- Python 3.x  
- Librerías: `numpy`, `matplotlib`, `scipy`, `tkinter`

## Uso
1. Ejecuta el archivo `prueba_medias.py`.  
2. Ingresa la cantidad de números (`n`) y el nivel de significancia (`α`).  
3. Presiona **Generar Prueba**.  
4. Observa la media muestral, los límites, el valor Z y el gráfico de los números Ri.

# Prueba de Varianza con Python y Tkinter

Este programa implementa una **prueba de hipótesis sobre la varianza** de números pseudoaleatorios generados con una distribución uniforme `U(0,1)`.  
La interfaz gráfica está hecha con **Tkinter** y utiliza **NumPy**, **Matplotlib** y **SciPy** para los cálculos y la visualización.

---

##  Descripción

El programa genera `n` números pseudoaleatorios en el intervalo `[0,1]` y calcula:

- La **varianza muestral (s²)**
- La **varianza teórica** de la distribución uniforme `U(0,1)` → `σ² = 1/12`
- El **estadístico Chi-cuadrado**:

\[
\chi^2 = \frac{(n-1) \cdot s^2}{\sigma^2}
\]

Luego compara este estadístico con los límites de aceptación de la prueba de hipótesis, usando el nivel de significancia `α`.

---

## ⚙️ Requisitos

Instalar las dependencias necesarias:

```bash
pip install numpy matplotlib scipy



# Prueba de Uniformidad con Chi-Cuadrado (Tkinter + Python)

Este programa implementa la **prueba de uniformidad Chi-Cuadrado** para verificar si un conjunto de números pseudoaleatorios generados por `U(0,1)` siguen una distribución uniforme.  
Incluye una interfaz gráfica con **Tkinter** que muestra los cálculos en una **tabla detallada** y un **histograma con frecuencias observadas y esperadas**.

---

## Descripción

La prueba compara las frecuencias observadas `Oi` en cada intervalo con las frecuencias esperadas `Ei = n/k`, calculando el estadístico:

\[
\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}
\]

Donde:

- `n` = número de valores generados
- `k` = número de intervalos
- `α` = nivel de significancia
- `df = k - 1` = grados de libertad

Se acepta o rechaza la hipótesis nula **H₀: los datos siguen una distribución uniforme en [0,1]**.

---

## ⚙️ Requisitos

Instalar dependencias:

```bash
pip install numpy matplotlib scipy
