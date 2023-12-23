import pyautogui
import time
import re


def wait():
    print("停顿")
    time.sleep(0.3)


def callMusic(data):
    if data.find(' ') >= 0:
        for s in str.split(data, ' '):
            wait()
            if s == '':
                wait()
            else:
                callMusic(s)
    else:
        dosarr = []
        for dos in data:
            dosarr.append(dos)
        print(dosarr)
        pyautogui.hotkey(dosarr)


def start():
    print("将于3秒后开始播放,请尽快切换至游戏...")
    time.sleep(3)
    music_str = open('music.txt', 'r').read()
    callMusic(music_str)

start()
print("播放完成..")
