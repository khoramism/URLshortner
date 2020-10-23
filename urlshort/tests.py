from django.test import TestCase

# Create your tests here.
 fixture from ``.
import json
import pytest
from graphene_django.utils.testing import graphql_query

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

# Test you query using the client_query fixture
def test_some_query(client_query):
    response = client_query(
        '''
        query {
            urls {
                id
                full
                hashedFull
            }
        }
        ''',
        op_name='urls'
    )

    content = json.loads(response.content)
    assert 'یک جایی داری اشتباه میزنی داوش' not in content
