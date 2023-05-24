import subprocess

version = subprocess.check_output("git describe --tags", shell=True).decode().strip().split('-')[0]
