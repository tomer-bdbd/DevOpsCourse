import getpass
import signal
import sys

username = getpass.getuser()
print(f"Hello! You are {username}")
print("Application running... Use 'kubectl delete pod' to stop")


def signal_handler(signum, frame):
    print(f"Received signal {signum}. Shutting down...")
    sys.exit(0)


signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

try:
    signal.pause()
except KeyboardInterrupt:
    print("Shutting down...")

