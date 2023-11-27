
from django.urls import path, include
from API_MUSIC.views.EspInfoView import EspInfoViewSet # Certifique-se de importar a classe EspInfoViewSet corretamente

urlpatterns = [
    path('', EspInfoViewSet.as_view({ 'post': 'create','get':'list'}), name='esp-info-list-create'),
]