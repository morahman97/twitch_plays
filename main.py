import socket
import logging
import time
# from collections import defaultdict
# import pyautogui
# import pydirectinput
import keyboard
import win32api
import win32con
# from pynput.mouse import Button, Controller

# Full list of character mappings can be found at https://raw.githubusercontent.com/SerpentAI/SerpentAI/dev/serpent/input_controllers/native_win32_input_controller.py
ds1_keymap = {
    'up': 0x11, # w
    'left': 0x1E, # a
    'down': 0x1F, # s
    'right': 0x20, # d
    'dup': 0xC8 + 1024, #arrowup
    'dleft': 0xCB + 1024, #arrowleft
    'ddown': 0xD0 + 1024, #arrowdown
    'dright': 0xCD + 1024, #arrowright
    'cup': 0x17, # i
    'cleft': 0x24, # j
    'cdown': 0x25, # k
    'cright': 0x26, # l
    'r3': 0x18, # o
    'l1': 0x2C, # z
    'l2': 0x2D, # x
    'r1': 0x23, # h
    'r2': 0x16, # u
    's': 0x12, # e
    'sq': 0x12, # e
    'square': 0x12, # e
    't': 0x2E, # c
    'tri': 0x2E, # c
    'triangle': 0x2E, # c
    'o': 0x2F, # v
    'circle': 0x2F, # v
    'x': 0x30, # b
    'start': 0x31, # n
    'select': 0x22 # g
}

def press(key):
    key = key.lower()
    delay = 0.2
    # If input command is to move, set a higher duration for movement
    if key == 'up' or key == 'left' or key == 'down' or key == 'right':
        delay = 0.5
    direct = ds1_keymap.setdefault(key,'')
    print(direct)
    if direct != '':
        keyboard.PressKey(direct)
        time.sleep(delay)
        keyboard.ReleaseKey(direct)

# Function to detect clicks specifically. Not used currently but can be used for other games that require mouse input
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('Left Click')


if __name__ == '__main__':
    print("Initializing Twitch Connection...")
    sock = socket.socket()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s — %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'mohomie' # rename this to streamer name
    token = 'oauth:5bcb60h4009zv85rqbh09p0vqmellz' # generate your own specific token using this link here... https://twitchapps.com/tmi/
    channel = '#mohomie' # rename this to streamer name with a '#' in front of it

    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    print("Listening...")
    while True:
        resp = sock.recv(2048).decode('utf-8')
        if len(resp) > 0:
            print("NEW MESSAGE: " + resp)
            key = resp.split()[-1][1:]
            print(key)
            press(key)