# Simulador de Distribuciones

Este proyecto es una **aplicación de escritorio en Python** que permite generar y visualizar datos aleatorios basados en distintas distribuciones estadísticas. La interfaz gráfica está construida con **Tkinter**, y se incluyen gráficos generados con **Matplotlib**.

---

## Características

- Generación de valores aleatorios según las siguientes distribuciones:
  - Uniforme
  - k-Erlang
  - Exponencial
  - Gamma
  - Normal
  - Weibull

- Visualización de los valores generados en una **tabla** con scroll horizontal y vertical.

- Representación gráfica de la **frecuencia de los valores** mediante un **histograma** interactivo.

- Interfaz con **scroll vertical global** para manejar contenido extenso.

- Validaciones de entrada:
  - Cantidad de valores mayor que cero.
  - Parámetros válidos según la distribución seleccionada.

---

## Requisitos

- Python 3.x
- Bibliotecas de Python:
  - `numpy`
  - `matplotlib`
  - `tkinter` (incluido con Python estándar)

Instalación de dependencias:

```bash
pip install numpy matplotlib

# 🎲 Simulador de Distribuciones Discretas

Este proyecto es una **aplicación de escritorio en Python** que permite generar y visualizar **distribuciones discretas** mediante gráficos de barras. La interfaz está desarrollada con **Tkinter** y los gráficos se crean con **Matplotlib**.

---

## Características

- Generación de valores aleatorios para las siguientes distribuciones discretas:
  - Uniforme discreta
  - Bernoulli
  - Binomial
  - Poisson

- Interfaz con scroll vertical para manejar cómodamente todo el contenido.

- Visualización de los datos generados mediante **histogramas**.

- Interfaz moderna con **colores agradables**, botones con efecto hover y diseño limpio.

- Parámetros dinámicos: según la distribución seleccionada, se muestran los campos necesarios.

---

## Requisitos

- Python 3.x
- Bibliotecas necesarias:
  - `numpy`
  - `matplotlib`
  - `tkinter` (incluido con Python estándar)

Instalación de dependencias:

```bash
pip install numpy matplotlib


# 🎮 Juego de la Vida Aleatorio

Este proyecto es una **implementación del Juego de la Vida de Conway** en Python, con un toque de aleatoriedad y funcionalidades adicionales. La interfaz gráfica se creó usando **Tkinter**, y permite visualizar cómo evolucionan las células en una cuadrícula siguiendo reglas simples.

---

## Características

- **Simulación aleatoria inicial:** La cuadrícula se llena aleatoriamente con células vivas según una probabilidad inicial configurable (`init_prob` = 0.2 por defecto).
- **Interactividad:**
  - Hacer clic en cualquier celda para activarla o desactivarla.
  - Botones para **Iniciar**, **Detener**, **Limpiar** y **Reiniciar** la simulación.
- **Detección de esquinas:** Si una célula llega a alguna esquina de la cuadrícula, la simulación se detiene y pregunta si deseas reiniciar.
- **Reglas clásicas de Conway:**
  - Una célula viva con 2 o 3 vecinos vivos sobrevive.
  - Una célula muerta con exactamente 3 vecinos vivos nace.
- **Visualización clara:** Celdas vivas en negro y celdas muertas en blanco/azul claro.

---

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)
- `ttk` para botones estilizados

---

## Uso

1. Ejecuta el script:

```bash
python juego_de_la_vida_random.py
