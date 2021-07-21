import sys
import re
import socket
import logging
import time
import keyboard
import win32api
import win32con

# Full list of character mappings can be found at https://raw.githubusercontent.com/SerpentAI/SerpentAI/dev/serpent/input_controllers/native_win32_input_controller.py
# ds1_keymap = {
#     'forward': 0x11, # w
#     'left': 0x1E, # a
#     'back': 0x1F, # s
#     'right': 0x20, # d
#     'dup': 0xC8 + 1024, #arrowup
#     'dleft': 0xCB + 1024, #arrowleft
#     'ddown': 0xD0 + 1024, #arrowdown
#     'dright': 0xCD + 1024, #arrowright
#     'cup': 0x17, # i
#     'cleft': 0x24, # j
#     'cdown': 0x25, # k
#     'cright': 0x26, # l
#     'r3': 0x18, # o
#     'l1': 0x2C, # z
#     'l2': 0x2D, # x
#     'r1': 0x23, # h
#     'r2': 0x16, # u
#     'sq': 0x12, # e
#     'square': 0x12, # e
#     'tri': 0x2E, # c
#     'triangle': 0x2E, # c
#     'o': 0x2F, # v
#     'circle': 0x2F, # v
#     'x': 0x30, # b
#     'start': 0x31, # n
#     'select': 0x22 # g
# }

ds1_keymap = {
    'forward': 0x11, # w
    'left': 0x1E, # a
    'back': 0x1F, # s
    'right': 0x20, # d
    'dup': 0x1B, # ]      # switch magic ]
    'dleft': 0x0C, # -    # switch left -
    'ddown': 0X1A, # [    # switch item [
    'dright': 0x0D, # =   # switch right weapon =
    'menuup': 0x32, # m      # select up m
    'mup': 0x32, # m      # select up m
    'menuleft': 0x21, # f    # select left f
    'mleft': 0x21, # f    # select left f
    'menudown': 0x15, # y    # select down y
    'mdown': 0x15, # y    # select down y
    'menuright': 0x19, # p    # select right p
    'mright': 0x19, # p    # select right p
    'camup': 0x17, # i
    'cup': 0x17, # i
    'camleft': 0x24, # j
    'cleft': 0x24, # j
    'camdown': 0x25, # k
    'cdown': 0x25, # k
    'camright': 0x26, # l
    'cright': 0x26, # l
    'r3': 0x18, # o
    'l1': 0x2C, # z
    'l2': 0x2D, # x
    'r1': 0x23, # h
    'r2': 0x16, # u
    'sq': 0x12, # e
    'square': 0x12, # e
    'tri': 0x2E, # c
    'triangle': 0x2E, # c
    'o': 0x2F, # v
    'circle': 0x2F, # v
    'x': 0x30, # b
    'enter': 0x30, # b
    'start': 0x31, # n
    'select': 0x22 # g
}

ACTIVE = False
blocking = False # flag used for determining if character holding block or not
sprinting = False # flag used for determining if character holding sprint or not

dodgeSet = {'dodge', 'dodgeleft', 'dodgeright', 'dodgeback'}

def dodge(key):
    global sprinting
    delay = 0.1
    if sprinting:
        keyboard.ReleaseKey(ds1_keymap['o'])
        time.sleep(delay)
    if key == '':
        keyboard.PressKey(ds1_keymap['forward'])
        keyboard.PressKey(ds1_keymap['circle'])
        time.sleep(delay)
        keyboard.ReleaseKey(ds1_keymap['forward'])
        keyboard.ReleaseKey(ds1_keymap['circle'])
    else:
        keyboard.PressKey(ds1_keymap[key])
        keyboard.PressKey(ds1_keymap['circle'])
        time.sleep(delay)
        keyboard.ReleaseKey(ds1_keymap[key])
        keyboard.ReleaseKey(ds1_keymap['circle'])
    if sprinting:
        time.sleep(delay)
        keyboard.PressKey(ds1_keymap['o'])

def press(key):
    global blocking
    global sprinting
    key = key.lower()
    if key == 'l1' and blocking: return
    delay = 0.1
    # If input command is to move or block, set a higher duration for action
    if key == 'forward' or key == 'left' or key == 'back' or key == 'right' or key == 'l1':
        delay = 0.5
    elif key == 'toggleblock':
        if blocking: 
            keyboard.ReleaseKey(ds1_keymap['l1'])
            blocking = False
        else:
            keyboard.PressKey(ds1_keymap['l1'])
            blocking = True
        return
    elif key == 'togglesprint':
        if sprinting:
            keyboard.ReleaseKey(ds1_keymap['o'])
            sprinting = False
        else:
            keyboard.PressKey(ds1_keymap['start'])
            time.sleep(0.1)
            keyboard.ReleaseKey(ds1_keymap['start'])
            time.sleep(0.1)
            keyboard.PressKey(ds1_keymap['o'])
            sprinting = True
        return
    elif key in dodgeSet:
        if key[:5] == 'dodge':
            dir = key[5:] # extract dodge direction
            dodge(dir)
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
    
    print("Initializing Parameters...")
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'mohomie' # rename this to streamer name
    token = 'oauth:5bcb60h4009zv85rqbh09p0vqmellz' # replace with your own token using link here... https://twitchapps.com/tmi/
    channel = '#mohomie' # rename this to streamer name with a '#' in front of it

    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    print("Listening...")
    while True:
        resp = sock.recv(512).decode('utf-8') # chat single message limit is 500
        if len(resp) > 0:
            # Reply to a PING with a PONG to ensure we don't time out
            print("NEW MESSAGE: " + resp)
            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            else:
                key = resp.split()[-1]
                if key[0] == ':': 
                    key = key[1:]
                    if key == 'EXIT' and (resp.startswith(':napstarf!') or resp.startswith(':mohomie!')):
                        print("-----------------ADMIN STOP---------------")
                        sys.exit()
                    elif key == 'PAUSE' and (resp.startswith(':napstarf!') or resp.startswith(':mohomie!')):
                        print("-----------------ADMIN PAUSE---------------")
                        ACTIVE = False
                    elif key == 'START' and (resp.startswith(':napstarf!') or resp.startswith(':mohomie!')):
                        print("-----------------ADMIN START---------------")
                        ACTIVE = True
                    else:
                        
                        if ACTIVE: 
                            print('ATTEMPTING TO PRESS ' + key)
                            press(key)
                        else: print("CHAT COMMANDS CURRENTLY PAUSED")

# NEW MESSAGE: :lokoheimer!lokoheimer@lokoheimer.tmi.twitch.tv PRIVMSG #mohomie :cleft