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

        if now not in data:
            data[now] = {
                'data': serializer.validated_data['dataHora'].strftime("%Y-%m-%d %H:%M:%S"),
                'valor': serializer.validated_data['valor']
            }
        print(data) 
        return Response(data)
    
    def delete(self, request):
        data.clear()
        return Response(status=status.HTTP_200_OK)


class EstatisticaView(APIView):
    def get(self, request):
        if not data:
            return Response('0', status=status.HTTP_204_NO_CONTENT)
        
        
        count = len(data)
        amount = sum(item['valor'] for item in data.values())
        avg = amount / count
        max_ = max(item['valor'] for item in data.values())
        min_ = min(item['valor'] for item in data.values())

        estatistica = {
            'count': count,
            'sum': amount,
            'avg': avg,
            'min': min_,
            'max': max_
        }
        return Response(estatistica, status=status.HTTP_200_OK)