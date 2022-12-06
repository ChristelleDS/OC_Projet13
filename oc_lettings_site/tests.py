from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from http import HTTPStatus


@pytest.fixture
def client():
    return Client()


class Test_Main(TestCase):

    def test_index(self, client):
        endpoint = reverse('main:index')
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        assert "Welcome" in response.content.decode()
