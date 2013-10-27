#!/usr/bin/python
import sys, signal, argparse, time, requests, pynotify

def signal_handler(signal, frame):
        print 'Exiting...'
        sys.exit(0)

def main(args):
  verbose = args.verbose
  token = args.token
  show_reward = args.reward
  no_gui = args.nogui
  update = args.update
  url = 'http://mining.bitcoin.cz/stats/json/' + token
  last = None
  pynotify.init('SlushBlockNotify')

  while True:
    try:
      r = requests.get(url)
      status = r.status_code
      r.raise_for_status()
      data = r.json()
    except requests.exceptions.ConnectionError, e:
      print 'Connection Error. Retrying in %i seconds' %update
      status = -2
    except Exception, e:
      pass

    if status == 401:
      print 'Unauthorized, check your token.'
      sys.exit(0)

    if status == 200:
      # The rows in the JSON ar not sorted, so we have to handle that
      row = data['blocks']
      blocks = row.keys()
      blocks.sort()
      # Get the last blocks NR
      current = blocks[-1]
      # Get the last blocks values
      values = row[blocks[-1]]

      if last is None:
        # First block after the program has started.
        # Only need the Block NR for further reference.
        if verbose: print 'First block for reference: %s' %current
        last = current
      elif last != current:
        # Set message for newly found block.
        # This depends on the passed flags via cmd.
        msg = None
        if show_reward:
          if 'reward' in values:
            msg = 'Time: %s<br />Duration: %s<br />Reward: %s' %(values['date_found'].split()[1], values['mining_duration'], values['reward'])
          else:
            if verbose: print 'Waiting for reward to be calculated'
        else:
          msg = 'Time: %s<br />Duration: %s' %(values['date_found'].split()[1], values['mining_duration'])

        if msg:
          if verbose: print 'Displaying notification'
          last = current
          if no_gui: print "#####\n" + msg.replace('<br />','\n')
          else:
            pynotify.Notification( 'New Block found', msg).show()

    time.sleep(update)

parser = argparse.ArgumentParser(description='Display notifications about newly found blocks on slush\'s pool.')
parser.add_argument('token',
                    metavar = 'API_TOKEN',
                    help = 'Slush pool API token. Can be found on your account page.')

parser.add_argument('-r',
                    '--reward',
                    dest = 'reward',
                    action = 'store_true',
                    help = 'Show reward per block. This will cause the notification to be shown as soon as your reward has been calculated by the pool.')

parser.add_argument('--nogui',
                    dest = 'nogui',
                    action = 'store_true',
                    help = 'No GUI, only show command line output.')

parser.add_argument('-v',
                    '--verbose',
                    dest = 'verbose',
                    action = 'store_true',
                    help = 'Show verbose information.')

parser.add_argument('-u',
                    '--update',
                    dest = 'update',
                    metavar = 'SEC',
                    type = int,
                    default = 90,
                    help = 'The update interval in seconds.')

signal.signal(signal.SIGINT, signal_handler)
args = parser.parse_args()
main(args)
