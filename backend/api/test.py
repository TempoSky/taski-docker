from http import HTTPStatus

from django.test import Client, TestCase

from api import models


class TaskiAPITestCase(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_list_exists(self) -> None:
        """Проверка доступности списка задач"""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self) -> None:
        """Проверка создания задачи"""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
