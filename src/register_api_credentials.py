"""
This script registers the uid and api_key defined in `src/api_credentials.json`
for usage in the era5cli.  
You can find your UID and API key in your user profile when you are logged in
on the [Copernicus Climate Data Store]https://cds.climate.copernicus.eu).

api_credentials.json must have the following structure:

```json
{
    "uid": ID_NUMBER,
    "api_key": "API_KEY"
}
```

"""

import json
import subprocess
import os

# get current file location
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# read api_credentials.json
with open(os.path.join(__location__, "api_credentials.json"), "r") as f:
    api_credentials = json.loads(f.read())

# get uid and api key
uid = api_credentials["uid"]
api_key = api_credentials["api_key"]

# cli command
cmd_str = f"era5cli config --uid {uid} --key '{api_key}'"

# register api key to era5cli
subprocess.Popen(cmd_str, shell=True)
