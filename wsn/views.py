from django.conf.urls import include, url
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from wsn.serializers import ConfiguracionSerializers, DatoSerializers, DatosTablaLabUnoSerializers, DatosTablaCampoUnoSerializers
from wsn.models import Dato, Locacion, BatteryLife, DatosLabUno, DatosCampoUno, LocacionesNodo,Configuracion_wsn
from django_datatables_view.base_datatable_view import BaseDatatableView
from braces.views import GroupRequiredMixin

"""#Index View"""
@login_required
def main_page(request):
    object = request.POST.get('next',None)
    if object is not None:
        return redirect(request.POST.get('next'))
    else:
        #if request.user.is_authenticated():
        username = request.user.username
        #username = request.POST.get('username')
        if username == 'yachtclub':
            return redirect('wsn/yachtclub-sf/') #redirect to yatchclub view
        else:
            return redirect('wsn/lab-test/1/')

"""#Lab Test Views """
#Redirect to lab_uno
@login_required
def lab_page(request):
    return redirect('1/')

@login_required
def lab_uno_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Laboratorio Nro. 1') #locaciones lab
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de Laboratorio Nro. 1', data__lte = 3.95 ) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    return render(request, 'wsn/lab_uno.html', {'locaciones':locaciones, 'bat':bat})

@login_required
def lab_dos_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Laboratorio Nro. 2') #locaciones lab
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de Laboratorio Nro. 2', data__lte = 3.95 ) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    #return render(request, 'wsn/lab_dos.html', {'locaciones':locaciones, 'bat':bat})
    return render(request, 'wsn/en_construccion_lab.html', {'locaciones':locaciones, 'bat':bat})

"""#Campo Test Views """
#Redirect to campo_uno
@login_required
def campo_page(request):
    return redirect('1/')

@login_required
def campo_uno_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Campo Nro. 1')
    #bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de campo Nro. 1', data__lte = 3.95) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    #return render(request, 'wsn/campo_uno.html', {'locaciones':locaciones, 'bat':bat})
    return render(request, 'wsn/campo_uno.html', {'locaciones':locaciones} )

@login_required
def campo_dos_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Campo Nro. 2')
    bat = BatteryLife.objects.all().filter(wsn_descrip='Prueba de campo Nro. 2', data__lte = 3.95) # tension de nodos lab / menores a 3.8 bateria baja (lte <=)
    #return render(request, 'wsn/starter.html', {'locaciones':locaciones, 'bat':bat})
    return render(request, 'wsn/en_construccion_campo.html', {'locaciones':locaciones, 'bat':bat})


"""Vista personalizada para el Yacthclub"""
@login_required
def yachtclub_page(request):
    locaciones = LocacionesNodo.objects.all().filter(wsn_descrip='Prueba de Campo Nro. 1')
    return render(request, 'wsn/yachtclub.html', {'locaciones':locaciones} )

"""#REST views--------------------------"""
class DatoList(GroupRequiredMixin,ListCreateAPIView):
    #permission_required = "auth.change_user"
    #required
    group_required = [u"arduino", u"administradores"]
    queryset = Dato.objects.all()
    serializer_class = DatoSerializers

class ConfiguracionList(ListCreateAPIView):
    queryset = Configuracion_wsn.objects.all()
    serializer_class = ConfiguracionSerializers

"""#Genero el Json para las graficas. Recordar que son las ultimas dos semanas"""
"""
LoginRequiredMixin herera todos los atributos del login seteados en el sistema. Es por esto,
que no es necesario configurar ningun parametro
"""
class DatosGraphLab_Uno_List(LoginRequiredMixin, ListAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = DatosLabUno.objects.all()
    serializer_class = DatosTablaLabUnoSerializers

"""#datatables Json generator"""
class DatosTableLab_Uno_List(LoginRequiredMixin, BaseDatatableView):
    model = DatosLabUno
    columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data','fecha_hora_text']
    order_columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data', 'fecha_hora_text']

#Faltan las siguientes vista:
#--Lab
#DatosGraphLab_Dos_List
#DatosTableLab_Dos_List
#--Campo
class DatosGraphCampo_Uno_List(LoginRequiredMixin, ListAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = DatosCampoUno.objects.all()
    serializer_class = DatosTablaLabUnoSerializers

"""#datatables Json generator"""
class DatosTableCampo_Uno_List(LoginRequiredMixin, BaseDatatableView):
    model = DatosCampoUno
    columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data','fecha_hora_text']
    order_columns = ['nodo', 'rol', 'tipo_sensor', 'sensor', 'data', 'fecha_hora_text']
#DatosTableCampo_Dos_List
#DatosTableCampo_Uno_List
#DatosTableCampo_Dos_List
