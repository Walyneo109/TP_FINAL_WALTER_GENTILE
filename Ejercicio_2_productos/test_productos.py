import pytest
import os
import json
from Ejercicio_2_productos.Productos import PanelSolar, StockInvalidError, GestorInventario

def test_precio_crudo_lanza_value_error():
   
    panel = PanelSolar("P-101", "Panel EcoVolt", "125000.00", 15, "21.5%", 450)
    
    with pytest.raises(ValueError):
        panel.gen_ficha_tecnica()


def test_stock_negativo_lanza_stock_error():
    
    with pytest.raises(StockInvalidError):
        PanelSolar("P-102", "Panel EcoFail", 85000.00, -4, "18%", 300)


def test_guardar_json_valido(tmp_path):
    
    panel = PanelSolar("P-103", "Celda Flex", 45000.50, 8, "19.0%", 200)
    ruta_json = tmp_path / "catalogo_ecotech.json"
    
    GestorInventario.guardar_catalogo_json([panel], str(ruta_json))
    
    assert os.path.exists(ruta_json)
    with open(ruta_json, "r", encoding="utf-8") as f:
        datos = json.load(f)
    assert datos[0]["id_product"] == "P-103"