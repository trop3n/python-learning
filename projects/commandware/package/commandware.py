import socket
import json
from pythonosc import udp_client
import requests

# ProPresenter Settings
PROP_IP = "192.168.1.100"
PROP_PORT = 8000

# ETC Settings
ETC_IP = "192.168.1.101"
ETC_PORT = 8001

# Widget Designer Settings
WD_IP = "192.168.1.102"
WD_PORT = 8080

# Map slides to actions (customize this)
SLIDE_ACTIONS = {
    0: {"etc_cue": 1, "wd_command": "start_intro"},
    1: {"etc_cue": 2, "wd_command": "play_video"}
}

# Connect to ETC via OSC
osc_client = udp_client.SimpleUDPClient(ETC_IP, ETC_PORT)

# Listen to ProPresenter
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((PROP_IP, PROP_PORT))

while True:
    data = s.recv(1024)
    if data:
        message = json.loads(data.decode())
        if message.get("action") == presentationSlideIndex":
            current_slide = message.get("slideIndex")
            action = SLIDE_ACTIONS.get(current_slide)
            if action:
                # trigger ETC cue
                osc_client.send_message(f"/eos/cue/{action['etc_cue']}/fire", [])
                # trigger WD command
                requests.get(f"http://{WD_IP}:{WD_PORT}/api/{action['wd_command']}")

