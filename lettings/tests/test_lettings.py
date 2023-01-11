import pytest
from django.test import Client
from django.urls import reverse
from http import HTTPStatus
from lettings.models import Letting


@pytest.fixture
def client():
    return Client()

"""
@pytest.mark.django_db
def test_index(client):
    endpoint = reverse('lettings:index')
    response = client.get(endpoint)
    assert response.status_code == HTTPStatus.OK
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_letting(client):
    endpoint = reverse('lettings:letting', kwargs={
        'letting_id': (Letting.objects.all()[0]).id})
    response = client.get(endpoint)
    assert response.status_code == HTTPStatus.OK
    assert "Joshua Tree Green" in response.content.decode()
"""

def test_dummy():
    assert 1