import os
import sys
import subprocess
from datetime import datetime as dt

from json2args import get_parameter

# parse parameters
kwargs = get_parameter()

# check if a toolname was set in env
toolname = os.environ.get('TOOL_RUN', 'era5_land').lower()

# switch the tool
if toolname == 'era5_land':
    # get the parameters
    try:
        variables, temporal_resolution = kwargs['variables'], kwargs['temporal_resolution']
        # get optional parameters
        startyear, endyear, area = kwargs.get('startyear', None), kwargs.get('endyear', None), kwargs.get('area', None)
    except Exception as e:
        print(str(e))
        sys.exit(1)
    
    # base command
    cmd_str = f"era5cli {temporal_resolution} --land --variables {variables}"

    # extent command with optional parameters if given
    if startyear:
        cmd_str += f" --startyear {startyear}"
    if endyear:
        cmd_str += f" --endyear {endyear}"
    if area:
        cmd_str += f" --area {area}"

    # split data monthly to avoid error message "Your request is too large for the CDS API."
    cmd_str += " --splitmonths True"

    print(cmd_str)

    # run the command
    subprocess.Popen(cmd_str, shell=True)

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
