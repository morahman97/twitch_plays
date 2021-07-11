import socket
import logging
import time
import pyautogui
import pydirectinput
import keyboard
import win32api
import win32con
from pynput.mouse import Button, Controller

# def press(key):
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
    nickname = 'mohomie'
    token = 'oauth:5bcb60h4009zv85rqbh09p0vqmellz'
    channel = '#mohomie'

    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    print("Initializing inputs...")
    mouse = Controller()

    print("Listening...")
    while True:
        # mouse.press(Button.left)
        # mouse.release(Button.left)
        # mouse.click(Button.left, 1)
        # pydirectinput.click()
        leftClick()
        # ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        # ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
        time.sleep(1)
        # autoit.mouse_click("left")
        # resp = sock.recv(2048).decode('utf-8')

        # if len(resp) > 0:
        #     print("NEW MESSAGE: " + resp)
        #     press = resp.split()[-1][1:]
        #     print(press)
        #     if press.lower() == "up":
        #         keyboard.PressKey(0x11)
        #         time.sleep(0.1)
        #         keyboard.ReleaseKey(0x11)
        #     if press.lower() == "r1":
        #         mouse.click(Button.left, 1)

        #     logging.info(resp)