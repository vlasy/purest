# puREST


puREST is a dead simple Python REST consumer based on [`requests`](http://docs.python-requests.org/en/master/) aiming for the simplest possible use while keeping all of the [`requests`](http://docs.python-requests.org/en/master/) features.

``` python
from purest import jsonplaceholder_typicode_com as api

posts = api.posts()
article = api.posts[1]()
comments = api.posts[1].comments()
```

# Installation

``` python 
pip install purest
```

# Basic usage

There are two main parts of puREST library. First one is concerned with the creation of puREST resources.

## Creating a puREST resource

puREST resource is a tiny wrapper above the [`requests`](http://docs.python-requests.org/en/master/) module. It provides magic methods for simpler and more straightforward use of REST endpoints.

As a first thing, you need to create the puREST resource. You can do it either directly or from an already existing puREST resource.

### Direct method

The most basic way of defining a puREST resource is creating a new instance of `Purest` class. You have to pass the desired URL to its constructor.

(I will demonstrate the library usage on the great [JSONPlaceholder website](https://jsonplaceholder.typicode.com/) where applicable)

``` python
from purest import Purest

api = Purest("https://jsonplaceholder.typicode.com/")
```

In addition to this method, you can even create the `Purest` resource right during the import from `purest` module. To do this, you have to import the camelCase name of URL from `purest`.

``` python
from purest import jsonplaceholder_typicode_com as api
```

The name you want to import is then transformed:

1) dot (`.`) is placed before each capital letter
2) string is converted to lowercase
3) `https://` is prepended
4) resulting string is used as an argument for `Purest` constructor

### Creating puREST object from another puREST object

If you already have a `Purest` instance pointing to some REST endpoint, it would be unpleasant to create new `Purest` resource for each other sub-endpoint on that site.

For that reason, you can easily create a new `Purest` object from any existing `Purest` object. It can be achieved either by getting its attribute or by getting its item.

``` python
from purest import jsonplaceholder_typicode_com as api

posts_url = api.posts
# equivalent to
posts_url = api['posts']
```

This also works for individual items of REST collections

``` python
from purest import jsonplaceholder_typicode_com as api

article)url = api.posts[1]
# equivalent to
article_url = api['posts'][1]
```

## Getting the puREST resource content

Once you have the `Purest` instance pointing to the desired endpoint, you can easily obtain its content by calling it.

As stated earlier, `Purest` is a [`requests`](http://docs.python-requests.org/en/master/) wrapper so you can also use the ordinary [`requests.get`](http://docs.python-requests.org/en/master/api/#requests.get) and the string you pass to that call will be appended to the URL the `Purest` object is pointing to.

``` python
from purest import jsonplaceholder_typicode_com as api

posts = api.posts()
# equivalent to
posts = api['posts']()
# equivalent to
posts = api.get('posts')

article = api.posts[1]()
# equivalent to
article = api.['posts'][1]()
```

# Advanced usage

For the simplest usage of REST possible, puREST makes some assumptions about the data obtained from the provided URLs.

By default, after GETting the response, it transforms it to JSON by [`requests.json()`](http://docs.python-requests.org/en/master/api/#requests.Response.json) method.

By default, all dictionaries in the response are enhanced with magic methods so that you can acces the dictionary items as if they would be attributes. This is done recursively (for embedded dictionaries as well). This behavior can be disabled by setting `transform_dict` to `False` in `Purest` constructor.

``` python
from purest import jsonplaceholder_typicode_com as api

article = api.posts[1]()

print article['id']
# equivalent to
print article.id
```

# Tests

```python setup.py test```