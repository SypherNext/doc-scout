import json
from datetime import datetime

data = {"timestamp": datetime.now()}

try:
    json.dumps(data)  # TypeError!
except TypeError as e:
    print(e)  # Object of type datetime is not JSON serializable


json.dumps(data, default=str)  # Converts everything to string
# Better: write a custom serializer specific to your types
