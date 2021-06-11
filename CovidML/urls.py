from django.contrib import admin
from django.urls import path
from CovidML.views import inicio,probabilidadMapa,calcular,nosotros
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('mapa/', probabilidadMapa),
    path('calcular/', calcular),
    path('nosotros/',nosotros),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
