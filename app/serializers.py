from rest_framework import serializers
from .models import VPS
from typing import Dict, Any


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ["uid", "cpu", "ram", "hdd", "status"]

    def create(self, validated_data: Dict[str, Any]) -> VPS:
        """
        Создание нового VPS с переданными данными
        """
        return VPS.objects.create(**validated_data)

    def update(self, instance: VPS, validated_data: Dict[str, Any]) -> VPS:
        """
        Обновление VPS с переданными данными
        """
        instance.cpu = validated_data.get("cpu", instance.cpu)
        instance.ram = validated_data.get("ram", instance.ram)
        instance.hdd = validated_data.get("hdd", instance.hdd)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
