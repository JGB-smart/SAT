from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import View

from tareas.models import Status, Prioridad, Tareas



@login_required
def estadisticas(request):

    return render(request,'estadisticas.html')



class estadisticasView(View):
    # form2 = RegistrationGroupForm(request.POST['grupo'])
    template_name = 'estadisticas.html'

    def get(self,request):
        # Contadores
        total_tareas = Tareas.objects.all().count() 
        # total_categoria = Tareas.objects.filter().count()
        # total_prioridad = Tareas.objects.filter().count()
        # total_status = Tareas.objects.filter().count()

        return render(
            request,
            self.template_name,
            {"total_tareas":total_tareas,
            "chart_prior": {
                "labels":["Importante_Urgente", "Importante_NoUrgente", "NoImportante_Urgente", "NoImportante_NoUrgente"],
                "values":[55, 10, 34]
            },
            "chart_stats": {
                "labels":["Finalizada", "Revisión", "En_Progreso", "No_Iniciada"],
                "values":[35, 22, 74, 94]
            },
            "chart_cat": {
                "labels":["Ventas"],
                "values":[155]
            },

            # "total_categoria": total_categoria,
            # "total_prioridad": total_prioridad,
            # "total_status": total_status,
            })
    