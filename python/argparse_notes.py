# parse command

import argparse

# ---------- Parse Arguments ------------
parser = argparse.ArgumentParser(description='Listen for commands from the agent')
parser.add_argument('-c', '--config', type=str, nargs='?',
                    help='Path to the config file.')

# on/off flag type - no arguments
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()
if vars(args)['config']:
    print(f'Parsed cmdline path to config file {vars(args)["config"]}')
    config_path = vars(args)['config']

print(vars(args)['verbose'])