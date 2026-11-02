import csv
def calcular_emisiones_carbono(consumo_kwh,
        factor_emision=0.4
):
    if consumo_kwh <0:
        raise ValueError(
            "El consumo no puede ser negativo"
        )
    return consumo_kwh * factor_emision
def cargar_registros_csv(route):
    registros = [] 
    with open(route, encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo) 
        for row in reader:
            row_limpio = {key.strip(): value for key, value in row.items()}
            registros.append({
                "planta": row_limpio["planta"],
                "consumo_kwh": float(row_limpio["consumo_kwh"])
            })
    return registros
def obtener_metricas_consumo (registros):
    total_emisiones = 0
    planta_mayor = max ( registros ,
                        key=lambda r: 
                        r["consumo_kwh"]
        )
    for reg in registros:
        total_emisiones += (calcular_emisiones_carbono(reg["consumo_kwh"])
        )
    return { 
        "total_emisiones":
        round(total_emisiones, 2), 
        "planta_mayor_consumo":
          planta_mayor["planta"]
    }
