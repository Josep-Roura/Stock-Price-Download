import yfinance as yf

# Descargar datos de Amazon (AMZN)
data = yf.download("AMZN", start="2023-01-01", end="2025-01-01")

# Guardar como CSV
data.to_csv("amazon_price_action.csv")

print("Archivo guardado como amazon_price_action.csv")
