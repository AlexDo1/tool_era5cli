import json
import subprocess
import os
from dotenv import load_dotenv


# load environment variables from a .env file in src/
load_dotenv()

def register_api_credentials():
    """
    This function registers the uid and api_key defined via environment variables.
    You can use a .env file stored in the folder `src/` or set the environment 
    variables `UID` and `API_KEY` manually in your environment.
    You can find your UID and API key in your user profile when you are logged in
    on the [Copernicus Climate Data Store]https://cds.climate.copernicus.eu).

    """
    uid = os.getenv("UID")
    api_key = os.getenv("API_KEY")

    # cli command
    cmd_str = f"era5cli config --uid {uid} --key '{api_key}'"

    # register api key to era5cli
    process = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and error (if any)
    output, error = process.communicate()

    # Convert the output from bytes to string
    output = output.decode('utf-8')

    print(output)
