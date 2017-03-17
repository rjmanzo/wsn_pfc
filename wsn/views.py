from django.conf.urls import include, url
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from wsn.serializers import ConfiguracionSerializers, DatoSerializers, DatosTablaLabSerializers
from wsn.models import Dato, Configuracion, Locacion, BatteryLife, DatosLab, LocacionesNodo
from django_datatables_view.base_datatable_view import BaseDatatableView

"""#App Principal"""
@login_required
def main_page(request):
    object = request.POST.get('next',None)
    if object is not None:
        return redirect(request.POST.get('next'))
    else:
        return redirect('wsn/lab-test/')

@login_required
def lab_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Laboratorio') #locaciones lab
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de Laboratorio', data__lte = 6) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    return render(request, 'wsn/starter.html', {'locaciones':locaciones, 'bat':bat})

@login_required
def campo_uno_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de campo Nro. 1')
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de campo Nro. 1', data__lte = 3.8) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    return render(request, 'wsn/starter.html', {'locaciones':locaciones, 'bat':bat})

@login_required
def campo_dos_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de campo Nro. 2')
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de campo Nro. 2', data__lte = 3.8) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    return render(request, 'wsn/starter.html', {'locaciones':locaciones, 'bat':bat})

"""#REST views--------------------------"""
class DatoList(ListCreateAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializers

class ConfiguracionList(ListCreateAPIView):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializers

"""#Genero el Json para las graficas. Recordar que son las ultimas dos semanas"""
"""
LoginRequiredMixin herera todos los atributos del login seteados en el sistema. Es por esto,
que no es necesario configurar ningun parametro
"""
class DatosGraphLabList(LoginRequiredMixin, ListAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = DatosLab.objects.all()
    serializer_class = DatosTablaLabSerializers

"""#datatables Json generator"""
class DatosTableLabList(LoginRequiredMixin, BaseDatatableView):
    model = DatosLab
    columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data','fecha_hora_text']
    order_columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data', 'fecha_hora_text']
