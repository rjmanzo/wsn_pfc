from django import forms
"""from wsn.models import Configuracion,Locacion
#from leaflet.forms.widgets import LeafletWidget

#create the form class.
#class LocacionForm(forms.Form):
#    class Meta:
#        model = Locacion
#        fields = '__all__'
#class ConfiguracionForm(forms.Form):
#    class Meta:
#        model = Configuracion
#        fields = '__all__'"""

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
