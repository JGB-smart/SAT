import locale
import calendar
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from tareas.models import Status, Prioridad, Tareas, Categorias



@login_required
def estadisticas(request):

    return render(request,'estadisticas.html')



class estadisticasView(View):
    # form2 = RegistrationGroupForm(request.POST['grupo'])
    template_name = 'estadisticas.html'

    def obtener_tareas_por_mes(self,):
        # Establecer el locale en español
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

        # Obtener el año actual
        anio_actual = datetime.now().year

        # Generar una lista de todos los meses del año con su respectivo nombre en español
        meses_del_anio = [datetime(anio_actual, mes, 1) for mes in range(1, 13)]
        nombres_meses = [mes.strftime('%B') for mes in meses_del_anio]

        # Consulta para obtener la cantidad de tareas por mes
        tareas_por_mes = Tareas.objects.filter(Fterminada__year=anio_actual).annotate(
            mes=ExtractMonth('Fterminada')).values('mes').annotate(total=Count('id'))

        # Crear un diccionario para almacenar los totales de tareas por mes
        totales_por_mes = {mes: 0 for mes in nombres_meses}

        # Actualizar el diccionario con los totales reales obtenidos de la consulta
        for tarea_mes in tareas_por_mes:
            mes_numero = tarea_mes['mes']
            mes_nombre = nombres_meses[mes_numero - 1]
            total = tarea_mes['total']
            totales_por_mes[mes_nombre] = total

        # Encontrar el mayor valor de "total"
        mayor_total = max(totales_por_mes.values())

        # Imprimir los totales de tareas por mes
        meses = [ {'mes': mes_nombre, 'total': total} for mes_nombre, total in totales_por_mes.items()]
        lista = [meses,mayor_total]
        return lista


    def get(self,request):
        # Contadores

        total_tareas = Tareas.objects.all().count() 

        status = Status.objects.all()
        counters_status = [ 
            {'label': i.status,
            'value': Tareas.objects.filter(status=i).count()} 
            for i in status]

        prioridad = Prioridad.objects.all()
        counters_prioridad = [ 
            {'label': i.prioridad,
            'value': Tareas.objects.filter(prioridad=i).count()} 
            for i in prioridad]

        categoria = Categorias.objects.all()
        counters_categoria = [ 
            {'label': i.categoria,
            'value': Tareas.objects.filter(categoria=i).count()} 
            for i in categoria]
        
        lista_p_mes = self.obtener_tareas_por_mes()
        


        return render(
            request,
            self.template_name,
            {"total_tareas":total_tareas,
            "cont_status": counters_status,
            "chart_stats": {
                "labels": [i['label'] for i in counters_status],
                "values":[i['value'] for i in counters_status]
            },
            "chart_prior": {
                "labels": [i['label'] for i in counters_prioridad],
                "values":[i['value'] for i in counters_prioridad]
            },
            "chart_cat": {
                "labels": [i['label'] for i in counters_categoria],
                "values":[i['value'] for i in counters_categoria]
            },
            "mes_chart":{
                "labels": [i['mes'] for i in lista_p_mes[0]],
                "values": [i['total'] for i in lista_p_mes[0]],
                "maximo": lista_p_mes[1],
            },
            })
    



''''
Contadores por status
    Recorer las prioridades, 
    y crear las cajas de contadores 

chart_stats

chart_prior:

Grafico de tareas por mes
========================
========================

tarea =  models.CharField(max_length=150,verbose_name='tarea')
descripcion =  models.CharField(max_length=200,verbose_name='descripcion')
status = models.ForeignKey(Status, on_delete=models.CASCADE,related_name='status_tarea')
prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE,related_name='prioridad_tarea')
categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE, related_name='categorias_tarea')
porcentaje = models.IntegerField(default=0)
CreadaPor = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'creador_tarea')
user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'asignaciones')
Fcreacion = models.DateTimeField(auto_now_add=True)
Ffinal = models.DateField()

'''

