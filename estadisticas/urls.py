from django.urls import path
from estadisticas.views import  estadisticasView


urlpatterns = [
     # path('', estadisticasView.estadisticas, name='estadisticas'),
     path(r'', estadisticasView.as_view(), name='estadisticas'),
]
