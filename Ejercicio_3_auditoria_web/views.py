from django.shortcuts import render
from django.shortcuts import redirect
from Emisiones import (cargar_registros_csv, obtener_metricas_consumo)
def vista_panel_sustentabilidad(request):
    registros = (
        cargar_registros_csv("Ejercicio_3_auditoria_web/Emisiones.csv")
    )
    context = (obtener_metricas_consumo(registros))
    context["registros"] = registros
    return render (request, "sustentabilidad/panel.html", context)
def redirigir_al_panel(request):
    return redirect('panel')
