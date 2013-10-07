# TODO
# * add option to display reward. This means the notification comes a little
#   later since the pool needs some time to calculate the reward
# * add an option to set the update interval, min should be 60 secs since
#   api calls are cached for 60 seconds.
#!/usr/bin/python
import sys, time, requests, subprocess

def main(argv):
  if len(argv) < 2:
    print "Usage sbn.py YOUR_SLUSH_API_TOKEN"
    return

  token = argv[1]
  url = "https://mining.bitcoin.cz/stats/json/" + token
  last = None

  while True:
    r = requests.get(url)
    data = r.json()

    # The rows in the JSON ar not sorted, so we have to handle that
    row = data["blocks"]
    blocks = row.keys()
    blocks.sort()
    
    key = blocks[-1]
    values = row[blocks[-1]]

    if last is None:
      last = key
      print "First: %s" %values
    elif last != key:
      print 'changed'
      if 'reward' in values:
        last = key
        msg = "@%s<br />Duration: %s<br />Reward: %s" %(values['date_found'], values['mining_duration'], values['reward'])
        print msg
        subprocess.Popen(['notify-send', 'New Block found', msg])

    time.sleep(90)

main(sys.argv)
