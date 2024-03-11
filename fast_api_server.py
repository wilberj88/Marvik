from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Contador para llevar registro de las llamadas a los endpoints
contador_llamadas = 0

@app.post("/obtener_fecha")
async def obtener_fecha(formateo: bool):
    global contador_llamadas
    contador_llamadas += 1

    if formateo:
        return {"fecha_actual": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {"fecha_actual": datetime.now().strftime("%Y-%d-%m")}

@app.get("/contador_llamadas")
async def obtener_contador_llamadas():
    global contador_llamadas
    return {"contador_llamadas": contador_llamadas}
