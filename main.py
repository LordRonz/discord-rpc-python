"""
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
"""

import os
import time

from pypresence import Presence

from options import get_options
from read_env import read_env


def main():
    read_env()
    client_id = os.getenv("CLIENT_ID")  # Enter your Application ID here.
    RPC = Presence(client_id=client_id)
    RPC.connect()

    # Make sure you are using the same name that you used when uploading the image

    while True:
        RPC.update(**get_options())
        time.sleep(15)  # Can only update presence every 15 seconds


if __name__ == "__main__":
    main()
