import random
import pyautogui
import time

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

keys = list(ds1_keymap.keys())
print(keys)

if __name__ == '__main__':
    while True:
        key = random.choice(keys)
        pyautogui.write(key)
        pyautogui.press('enter')
        time.sleep(1)