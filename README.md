Perfecto ✅ — aquí tienes un **README.md limpio y directo**, pensado para alguien que solo quiere **instalar la librería, ejecutar el código y ver los resultados**, sin explicaciones innecesarias.
Funciona para **cualquier acción** (no solo AMZN).

---

````markdown
# 📈 Descargar y analizar datos de acciones con Python

Este tutorial permite obtener y visualizar los precios históricos de **cualquier acción** usando Python, sin necesidad de descargar archivos manualmente.

---

## ⚙️ Requisitos

Instala las librerías necesarias ejecutando este comando en tu terminal o en una celda del notebook:

```bash
pip install yfinance pandas matplotlib
````

---

## 🚀 Ejecución

Abre tu editor o Jupyter Notebook y copia el siguiente código:

```python
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 🔹 Escribe aquí el ticker de la acción (por ejemplo, 'AAPL', 'AMZN', 'TSLA', 'MSFT')
ticker = "AAPL"

# 🔹 Descarga los datos (puedes ajustar las fechas)
Stock = yf.download(ticker, start="2024-01-01", end="2025-01-01")

# 🔹 Muestra las primeras filas
print(Stock.head())

# 🔹 Grafica el precio de cierre
plt.plot(Stock['Date'], Stock['Close'])
plt.title(f'Evolución del precio de {ticker}')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.grid(True)
plt.show()
```

---

## 🧠 Notas

* Puedes cambiar `"AAPL"` por cualquier otro **ticker** disponible en Yahoo Finance.
  Ejemplos:

  * Amazon → `"AMZN"`
  * Tesla → `"TSLA"`
  * Google → `"GOOG"`
  * Microsoft → `"MSFT"`
* El rango de fechas (`start` y `end`) puede modificarse libremente.
* La columna `'Close'` representa el precio de cierre diario.

---

## ✅ Resultado esperado

1. Una tabla con los precios descargados.
2. Un gráfico que muestra la evolución del precio de la acción en el periodo indicado.

---

## 👤 Autor

**Josep Roura Fernández**
📧 [joseprouraf@gmail.com](mailto:joseprouraf@gmail.com)
