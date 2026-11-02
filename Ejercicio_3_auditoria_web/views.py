from django.shortcuts import render
from Emisiones import (cargar_registros_csv, obtener_metricas_consumo)
def vista_panel_sustentabilidad(request):
    registros = (
        cargar_registros_csv("Ejercicio_3_auditoria_web/Emisiones.csv")
    )
    context = (obtener_metricas_consumo(registros))
    return render (request, "sustentabilidad/panel.html", context)