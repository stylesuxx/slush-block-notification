#### Slush's pool block notification
Get a notification when a new block was found in slushs pool. Also displays some additional information like duration and your your reward for that block. Slushs pool is queried every 90 seconds by default since API calls are cached for 60 seconds and we do not want to flood the server. Update interval may be adjusted via argument.

##### Dependencies:
* python 2.x
* libs: requests, [notify-python](http://galago-project.org/news/index.php)
* slush pool API token (available on your account page)

##### Possible Notifications
* Desktop
* Command line only
* E-Mail

##### E-Mail
If you want to use the email functionality you will need a local SMTP server. Check your spam folder for the notifications and make a rule to filter them.

##### Usage
```
usage: sbn.py [-h] [-r] [--nogui] [-e email] [-v] [-u SEC] API_TOKEN

Display notifications about newly found blocks on slush's pool.

positional arguments:
  API_TOKEN             Slush pool API token. Can be found on your account
                        page.

optional arguments:
  -h, --help            show this help message and exit
  -r, --reward          Show reward per block. This will cause the
                        notification to be shown as soon as your reward has
                        been calculated by the pool.
  --nogui               No GUI, only show command line output.
  -e EML, --email EML   Provide an email.
  -v, --verbose         Show verbose information.
  -u SEC, --update SEC  The update interval in seconds.
```
