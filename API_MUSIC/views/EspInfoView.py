from rest_framework import viewsets, status
from rest_framework.response import Response
from API_MUSIC.serializer.EspInfoSerializer import EspInfoSerializer
from API_MUSIC.models import EspInfoEntity  # Corrija a importação do modelo
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class EspInfoViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = EspInfoEntity.objects.all()  # Utilize o modelo correto EspInfoEntity
        serializer = EspInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EspInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Mantém o receiver para o sinal post_save, isso é parte da lógica do modelo EspInfoEntity
# jogar no ventilador
@receiver(post_save, sender=EspInfoEntity)
def reset_daily_data(sender, instance, **kwargs):
    if (timezone.now() - instance.ultima_atualizacao).days >= 1:
        instance.tempo_de_estudo = 0.0
        instance.ultima_atualizacao = timezone.now()
        instance.save()
