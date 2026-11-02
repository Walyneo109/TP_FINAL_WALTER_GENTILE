import pytest
from Emisiones import calcular_emisiones_carbono

class TestCalculoEmisiones:
    
    def test_calculo_valores_nominales(self):
        #Se valida la exactitud numérica ante valores normales#
        assert calcular_emisiones_carbono(100) == 40.0
        assert calcular_emisiones_carbono(50, factor_emision=0.5) == 25.0
        assert calcular_emisiones_carbono(0) == 0.0

    def test_excepcion_consumo_negativo(self):
        #Se prueba ValueError#
        with pytest.raises(ValueError):
            calcular_emisiones_carbono(-15)
