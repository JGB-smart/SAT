from django.urls import path
from home import views
from.views import salir


urlpatterns = [
    path('salir/', salir, name="salir" )
]
