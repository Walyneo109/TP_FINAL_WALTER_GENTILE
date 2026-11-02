import pytest
from sensores import (
    limpiar_registro_sensor,
    generar_resumen_sensores
)


def test_limpieza():
    dato = {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": " Planta Norte "
    }
    resultado = limpiar_registro_sensor(dato)

    assert resultado["sensor_id"] == "SENSOR-001"
    assert resultado["temperatura"] == 24.5
    assert resultado["ubicacion"] == "Planta Norte"
    
def test_ubicacion():
    dato = {
        "sensor_id": "S1",
        "temperatura": "20C",
        "ubicacion": ""
    }
    resultado = limpiar_registro_sensor(dato)

    assert (
        resultado["ubicacion"] == "Area no asignada"
    )

def test_resumen_sensores():

    sensores = [
        {
            "sensor_id": "A",
            "temperatura": 20
        },
        {
            "sensor_id": "B",
            "temperatura": 40
        }
    ]

    alertas, promedio = (
        generar_resumen_sensores(
            sensores,
            30
        )
    )

    assert alertas == ["B"]
    assert promedio == 30.0