#### Slush's pool block notification
Get a system notification when a new block was found in slushs pool. Also displays some additional information like duration and your your reward for that block. Slushs pool is queried every 90 seconds by default since API calls are cached for 60 seconds and we do not want to flood the server. Update interval may be adjusted via argument.

This should work cross plattform, although I have not tested it on Windows or Mac. Maybe someone could confirm that?

##### Dependencies:
* python 2.x
* libs: requests, pynotify
* slush pool API token (available on your account page)

##### Usage
```
usage: sbn.py [-h] [-r] [-u SEC] API_TOKEN

Display notifications about newly found blocks on slush's pool.

positional arguments:
  API_TOKEN             Slush pool API token. Can be found on your account
                        page.

optional arguments:
  -h, --help            show this help message and exit
  -r, --reward          Show reward per block. This will cause the
                        notification to be shown as soon as your reward has
                        been calculated by the pool.
  -u SEC, --update SEC  The update interval.
```
