#### Slush block notification
Get a system notification when a new block was found in slushs pool. Also displays some additional information like duration and your your reward for that block. Slushs pool is queried every 90 seconds since API calls are cached for 60 seconds and we do not want to flood the server.

This should work with all all linux distributions that use libnotify, which I think all major distributions do.

##### Dependencies:
* python
* libnotify-bin
* slush pool API token (available on your account page)

##### Usage
`./sbn.py YOUR_API_TOKEN`
