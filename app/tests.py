from rest_framework import status
from rest_framework.test import APITestCase
from .models import VPS
import uuid

class VPSApiTests(APITestCase):
    def setUp(self):
        """Создаём начальные данные для тестов"""
        self.vps_data = {
            "cpu": 4,
            "ram": 16,
            "hdd": 100,
            "status": "started"
        }
        self.url = "/api/v1/vps/"
        self.vps = VPS.objects.create(**self.vps_data)

    def test_create_vps(self):
        """Тестируем создание VPS"""
        response = self.client.post(self.url, self.vps_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("uid", response.data)
        self.assertEqual(response.data["cpu"], self.vps_data["cpu"])
        self.assertEqual(response.data["status"], self.vps_data["status"])

    def test_get_vps_list(self):
        """Тестируем получение списка всех VPS"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_vps_detail(self):
        """Тестируем получение данных о конкретном VPS"""
        response = self.client.get(f"{self.url}{self.vps.uid}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["uid"], str(self.vps.uid))

    def test_update_vps_status(self):
        """Тестируем изменение статуса VPS"""
        new_status = {"status": "blocked"}
        response = self.client.patch(f"{self.url}{self.vps.uid}/", new_status, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["new_status"], "blocked")

    def test_delete_vps(self):
        """Тестируем удаление VPS"""
        response = self.client.delete(f"{self.url}{self.vps.uid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(VPS.DoesNotExist, VPS.objects.get, uid=self.vps.uid)

    def test_invalid_status_change(self):
        """Тестируем попытку изменить статус на неверное значение"""
        invalid_status = {"status": "invalid_status"}
        response = self.client.patch(f"{self.url}{self.vps.uid}/", invalid_status, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Invalid status")