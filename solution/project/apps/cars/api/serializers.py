from rest_framework import serializers

from ..models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        depth = 1
        fields = (
            "name",
            "model",
            "year",
            "total_gas_capacity",
            "current_gas_capacity",
            "tyres",
        )
