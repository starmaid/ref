# parse command

import argparse

# ---------- Parse Arguments ------------
parser = argparse.ArgumentParser(description='Listen for commands from the agent')
parser.add_argument('--config', type=str, nargs='?',
                    help='Path to the config file.')

args = parser.parse_args()
if vars(args)['config']:
    print(f'Parsed cmdline path to config file {vars(args)["config"]}')
    config_path = vars(args)['config']