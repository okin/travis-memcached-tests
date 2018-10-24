# -*- coding: utf-8 -*-

import memcache  # python-memcached
import umemcache

ADDRESS = "127.0.0.1:11211"
KEY = 'testing'
VALUE = 'this is a test'


def test_memcache_client():
    print("memcache client creation")
    client = memcache.Client([ADDRESS], debug=1)
    print("Client is connected")

    set_value(client)
    get_value(client)


def test_umemcache_client():
    """Create a new Client object."""
    print("umemcache client creation")
    client = umemcache.Client(ADDRESS)
    client.connect()
    print("Client is connected")

    set_value(client)
    get_value(client)


def set_value(client):
    client.set(KEY, VALUE)


def get_value(client):
    print("Trying to get a value with {}...".format(client))
    try:
        value = client.get(KEY)
    except Exception as err:
        print("Caught exception: {!r}".format(err))
        return

    print(repr(value))
    assert VALUE == value


if __name__ == '__main__':
    test_memcache_client()
    test_umemcache_client()
