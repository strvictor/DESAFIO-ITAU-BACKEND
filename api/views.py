from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransacaoSerializer
from datetime import datetime

data = {} 
class TransacaoView(APIView):
    def post(self, request):
        serializer = TransacaoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST) if 'non_field_errors' in serializer.errors else Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data[now] = {
            'dataHora': serializer.validated_data['dataHora'].strftime("%Y-%m-%d %H:%M:%S"),
            'valor': serializer.validated_data['valor']
        }

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        data.clear()
        return Response(status=status.HTTP_200_OK)

class EstatisticaView(APIView):
    def get(self, request):
        now = datetime.now()

        recentes = {
            k: v for k, v in data.items()
            if (now - datetime.strptime(k, "%Y-%m-%d %H:%M:%S")).total_seconds() <= 60
        }

        if not recentes:
            return Response('0', status=status.HTTP_204_NO_CONTENT)

        valores = [item['valor'] for item in recentes.values()]
        estatistica = {
            'count': len(valores),
            'sum': sum(valores),
            'avg': sum(valores) / len(valores),
            'min': min(valores),
            'max': max(valores)
        }

        return Response(estatistica, status=status.HTTP_200_OK)
