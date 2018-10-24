# -*- coding: utf-8 -*-

import umemcache

ADDRESS = "127.0.0.1:11211"


def test_umemcache_client():
    """Create a new Client object."""
    print("umemcache client creation")
    client = umemcache.Client(ADDRESS)
    client.connect()
    print("Client is connected")

    print("Trying to get a value...")
    try:
        client.get("")
    except Exception as err:
        print("Caught exception: {!r}".format(err))


if __name__ == '__main__':
    test_umemcache_client()
