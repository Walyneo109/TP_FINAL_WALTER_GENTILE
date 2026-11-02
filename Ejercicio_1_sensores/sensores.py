## Punto A: normalizar lecturas ##

def limpiar_registro_sensor(registro_raw):
    reg_limpio = {}
    reg_limpio["sensor_id"] = (
        str(registro_raw.get("sensor_id", ""))
        .strip()
    )
    temperatura =  registro_raw.get("temperatura", 0)
    try:
        if isinstance(temperatura, (int,float)):
             temperatura = float(temperatura)
        else:
            temperatura = (
                str(temperatura)
                .replace("°","")
                .replace("C","")
                .replace("F", "")
                .replace(" ","")
            )
            temperatura= float(temperatura)
    except ValueError:
        temperatura = 0.0
    reg_limpio["temperatura"] = temperatura

    ubicacion = registro_raw.get("ubicacion")
    if ubicacion and str(ubicacion).strip():
        reg_limpio["ubicacion"] = (
            str(ubicacion)
            .strip()
        )
    else:
        reg_limpio["ubicacion"] = (
            "Area no asignada"
        )    
    return reg_limpio
## Punto B Genera un resumen de los sensores##
def generar_resumen_sensores(
        lista_sensores_limpios,
        umbral_temp
):
    if not lista_sensores_limpios:
        return [], 0.0
    suma = 0.0
    alertas= []
    
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma += temp
        if temp > umbral_temp:
            alertas.append(
                sensor["sensor_id"]
            )
    promedio = round( suma / len(lista_sensores_limpios),2)
    return alertas, promedio


##Pruebas con datos##
if __name__ == "__main__":
    Data = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "35.0 C", "ubicacion": "   "},
        {"sensor_id": " SENSOR-003  ", "temperatura": "31.2°C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "CORRUPTO", "ubicacion": "Laboratorio"}
    ]
    
    print("Probando Sanitización ")
    
    sensores_limpios = [limpiar_registro_sensor(r) for r in Data]
    for s in sensores_limpios:
        print(s)
        
    print("\n Reporte Estadístico")
    umbral = 30.0
    lista_alertas, promedio_total = generar_resumen_sensores(sensores_limpios, umbral)
    
    print(f"Umbral de alerta: {umbral}°C")
    print(f"Sensores en alerta: {lista_alertas}")
    print(f"Promedio térmico global: {promedio_total}°C")