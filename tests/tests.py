from django.test import TestCase
import pytest
from django.test import Client
from http import HTTPStatus


@pytest.fixture
def client():
    return Client()


class TestHome(TestCase):

    def test_index(self, client):
        # endpoint = reverse('index')
        response = client.get('')
        assert response.status_code == HTTPStatus.OK
        assert "Welcome" in response.content.decode()
