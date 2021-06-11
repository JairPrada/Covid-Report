from django.contrib import admin
from django.urls import path
from CovidML.views import inicio,probabilidadMapa,calcular,nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('mapa/', probabilidadMapa),
    path('calcular/', calcular),
    path('nosotros/',nosotros)
]
