from django.contrib import admin
from django.urls import path
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EJERCICIO_3_PATH = os.path.join(BASE_DIR, 'Ejercicio_3_auditoria_web')

if EJERCICIO_3_PATH not in sys.path:
    sys.path.insert(0, EJERCICIO_3_PATH)

from Ejercicio_3_auditoria_web.views import vista_panel_sustentabilidad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_panel_sustentabilidad, name='panel'),
]
