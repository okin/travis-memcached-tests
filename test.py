# -*- coding: utf-8 -*-

import memcache  # python-memcached
import umemcache

ADDRESS = "127.0.0.1:11211"


def test_memcache_client():
    print("memcache client creation")
    client = memcache.Client([ADDRESS], debug=1)
    print("Client is connected")

    get_value(client)


def test_umemcache_client():
    """Create a new Client object."""
    print("umemcache client creation")
    client = umemcache.Client(ADDRESS)
    client.connect()
    print("Client is connected")
    get_value(client)


def get_value(client):
    print("Trying to get a value with {}...".format(client))
    try:
        client.get("")
    except Exception as err:
        print("Caught exception: {!r}".format(err))


if __name__ == '__main__':
    test_memcache_client()
    test_umemcache_client()
