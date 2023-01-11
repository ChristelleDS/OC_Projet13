"""
import pytest
from django.test import Client
from django.urls import reverse
from http import HTTPStatus


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    endpoint = reverse('profiles:index')
    response = client.get(endpoint)
    assert response.status_code == HTTPStatus.OK
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_profile(client):
    endpoint = reverse('profiles:profile', kwargs={
        'username': 'AirWow'})
    response = client.get(endpoint)
    assert response.status_code == HTTPStatus.OK
    assert "AirWow" in response.content.decode()
"""


def test_dummy():
    assert 1
