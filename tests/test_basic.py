import pytest


@pytest.fixture
def api():
    from purest import jsonplaceholderTypicodeCom as api
    return api


def test_import_resolution():
    from purest import Purest
    from purest import jsonplaceholderTypicodeCom as api
    assert Purest == type(api)


def test_collection_get(api):
    result = api.get('posts')
    assert 100 == len(result)


def test_collection_url(api):
    result = api.posts
    assert "https://jsonplaceholder.typicode.com/posts/" == result._Purest__base_url


def test_collection_call(api):
    result = api.posts()
    assert 100 == len(result)


def test_collection_item_url(api):
    result = api['posts']
    assert "https://jsonplaceholder.typicode.com/posts/" == result._Purest__base_url


def test_collection_item_call(api):
    result = api['posts']()
    assert 100 == len(result)


def test_item_url(api):
    result = api.posts[1]
    assert "https://jsonplaceholder.typicode.com/posts/1/" == result._Purest__base_url


def test_item_get(api):
    result = api.posts.get(1)
    assert 1 == result['id']


def test_item_call(api):
    result = api.posts[1]()
    assert 1 == result['id']


def test_item_collection_url(api):
    result = api.posts[1].comments
    assert "https://jsonplaceholder.typicode.com/posts/1/comments/" == result._Purest__base_url
