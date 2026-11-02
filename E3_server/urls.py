from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EJERCICIO_3_PATH = os.path.join(BASE_DIR, 'Ejercicio_3_auditoria_web')

if EJERCICIO_3_PATH not in sys.path:
    sys.path.insert(0, EJERCICIO_3_PATH)

from Ejercicio_3_auditoria_web.views import vista_panel_sustentabilidad
from Ejercicio_3_auditoria_web.views import redirigir_al_panel



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirigir_al_panel, name='inicio'),
    path('sustentabilidad/panel', vista_panel_sustentabilidad, name='panel'),
]
