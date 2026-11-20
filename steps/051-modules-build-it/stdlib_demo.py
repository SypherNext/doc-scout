# stdlib_demo.py

# Single import
import os
print(os.getcwd())       # Current working directory

# Import with alias
import json as js
# js.load, js.dump, etc.

# Import specific names
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Import everything (avoid in production: pollutes namespace)
# from math import *
