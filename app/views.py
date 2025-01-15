from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VPS
from .serializers import VPSSerializer
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from typing import Optional

class VPSListCreateView(APIView):
    def get(self, request: Request) -> Response:
        """
        Вывод всех VPS с возможностью фильтрации
        """
        vps_list = VPS.objects.all()

        # Фильтрация по статусу (если передан параметр status)
        status_filter = request.query_params.get('status', None)
        if status_filter:
            vps_list = vps_list.filter(status=status_filter)

        # Сериализуем данные
        serializer = VPSSerializer(vps_list, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Создание нового VPS
        """
        serializer = VPSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VPSDetailView(APIView):
    def get(self, request: Request, uid: str) -> Response:
        """
        Получение данных о VPS по его UID
        """
        vps = get_object_or_404(VPS, uid=uid)
        serializer = VPSSerializer(vps)
        return Response(serializer.data)

    def patch(self, request: Request, uid: str) -> Response:
        """
        Обновление статуса VPS
        """
        vps = get_object_or_404(VPS, uid=uid)
        new_status = request.data.get('status')

        if new_status in dict(VPS.STATUS_CHOICES):
            vps.status = new_status
            vps.save()
            return Response({'status': 'updated', 'new_status': vps.status})

        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, uid: str) -> Response:
        """
        Удаление VPS
        """
        vps = get_object_or_404(VPS, uid=uid)
        vps.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)