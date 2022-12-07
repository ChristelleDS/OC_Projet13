import pytest
from django.test import Client
from django.urls import reverse
from http import HTTPStatus
from .models import Letting


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
class test_Lettings:
    def test_index(self, client):
        endpoint = reverse('lettings:index')
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        assert "Lettings" in response.content.decode()

    def test_letting(self, client):
        endpoint = reverse('lettings:letting', kwargs={
                'letting_id': (Letting.objects.all()[0]).id})
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        assert "Joshua Tree Green" in response.content.decode()
