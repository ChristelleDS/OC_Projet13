from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from http import HTTPStatus


@pytest.fixture
def client():
    return Client()


class TestLettings(TestCase):

    def test_index(self, client):
        endpoint = reverse('lettings:index')
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        # assert "Welcome" in response.content.decode()

    def test_letting(self, client):
        endpoint = reverse('lettings:letting')
        response = client.get(endpoint)
        assert response.status_code == HTTPStatus.OK
        # assert "Welcome" in response.content.decode()
