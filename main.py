'''
You need to upload your image(s) here:
https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
'''

from pypresence import Presence
import time
import json
from read_env import read_env
import os

def main():
    read_env()
    client_id = os.getenv('CLIENT_ID')  # Enter your Application ID here.
    RPC = Presence(client_id=client_id)
    RPC.connect()

    with open('./options.json', 'r') as j:
        options = json.load(j)

    # Make sure you are using the same name that you used when uploading the image
    RPC.update(**options)

    while True:
        time.sleep(15) #Can only update presence every 15 seconds

if __name__ == '__main__':
    main()
