from notebook.auth.security import passwd
import sys

print(passwd(passphrase=sys.argv[1]))