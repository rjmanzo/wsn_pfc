from django.conf.urls import include, url
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework.generics import ListCreateAPIView, ListAPIView
from wsn.serializers import ConfiguracionSerializers, DatoSerializers, DatosTablaLabSerializers #,LocacionesLabSerializers
from wsn.models import Dato, Configuracion, Locacion ,DatosTablaLab #,LocacionesLab
""" django.views.generic import TemplateView"""
from django_datatables_view.base_datatable_view import BaseDatatableView
from djgeojson.views import GeoJSONLayerView


"""#App Principal"""
@login_required
def main_page(request):
    #return HttpResponseRedirect(request.POST.get('next', none))
    object = request.POST.get('next',None)
    if object is not None:
        return redirect(request.POST.get('next'))
    else:
        return redirect('wsn/lab-test/')

@login_required
def lab_page(request):
    return render(request, 'wsn/starter.html', {})

@login_required
def campo_uno_page(request):
    return render(request, 'wsn/starter.html', {})

@login_required
def campo_dos_page(request):
    return render(request, 'wsn/starter.html', {})

"""#REST views--------------------------"""
class DatoList(ListCreateAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializers

class ConfiguracionList(ListCreateAPIView):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializers

"""#Genero el Json para las graficas. Recordar que son las ultimas dos semanas"""
class DatosTablaLabList(ListAPIView):
    queryset = DatosTablaLab.objects.all()
    serializer_class = DatosTablaLabSerializers

#"""#Genero el Json para las locaciones del mapa"""
#class LocacionesLabList(ListAPIView):
#    queryset = LocacionesLab.objects.all()
#    """#cuando entramos en esta vista mediante api-locations-lab nos carga directamente el Json
    # Esto sucede por que renderizamos con JSONRenderer y por q a su vez el parser por defecto es JSONParser
    #renderer_classes = (JSONRenderer, )
    #parser_classes = (JSONParser,)"""
#    serializer_class = LocacionesLabSerializers

"""#datatables Json generator"""
class TablaLabsListJson(BaseDatatableView):
    model = DatosTablaLab
    columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data','fecha_hora_text']
    order_columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data', 'fecha_hora_text']
