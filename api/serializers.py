from rest_framework import serializers
from datetime import datetime, timezone

class TransacaoSerializer(serializers.Serializer):
    valor = serializers.FloatField()
    dataHora = serializers.DateTimeField()

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor da transação não pode ser negativo.")
        return value

    def validate_dataHora(self, value):
        now = datetime.now(timezone.utc)  # Obtém a data/hora atual em UTC
        if value > now:
            raise serializers.ValidationError("A transação não pode estar no futuro.")
        return value
