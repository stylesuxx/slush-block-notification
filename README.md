#### Slush block notification
Get a system notification when a new block has been found in slush's pool and what your reward was. Slushs pool is queried every 90 seconds since API calls are cached for 60 seconds and we do not want to flood the server.

##### Dependencies:
* python
* libnotify-bin
* slush pool API token (available on your account page)

##### Usage
./sbn.py YOUR_API_TOKEN