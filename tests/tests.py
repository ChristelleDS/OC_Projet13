import pytest
from django.test import Client
from http import HTTPStatus

from django.urls import reverse


@pytest.fixture
def client():
    return Client()


class TestHome:

    def test_index(self, client):
        endpoint = reverse('index')
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        assert "Welcome to Holiday Homes" in response.content.decode()
