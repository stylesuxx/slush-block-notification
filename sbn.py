#!/usr/bin/python
import sys, time, requests, subprocess

def main(argv):
  if len(argv) < 2:
    print "Usage sbn.py API_TOKEN"
    return

  token = argv[1]
  url = "https://mining.bitcoin.cz/stats/json/" + token
  last = None

  while True:
    r = requests.get(url)
    data = r.json()
    row = data["blocks"].popitem()
    key = row[0]
    values = row[1]

    if last is None:
      last = key
    elif last != key:
      msg = "xx@%s<br />Duration: %s<br />Reward: %s" %(values['date_found'], values['mining_duration'], values['reward'])
      print msg
      subprocess.Popen(['notify-send', 'New Block found', msg])

    time.sleep(90)

main(sys.argv)