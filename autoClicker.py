import sys
import time
import threading
import random

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

"""
    Author: Benjamin Patch
    Dependencies: pynput
"""
delay = 1
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        pass

    def randomise(self, delay):
        randomiser:int = random.uniform(1, 10001)
        if randomiser == 1:
            # 0.01% chance of sleeping for between 3.5 and 4.95 minutes
            time.sleep(random.uniform(210, 297))
        elif randomiser > 1 and randomiser < 75:
            # 0.73% chance of sleeping between 10 and 21 seconds
            time.sleep(random.uniform(10, 21))
        elif randomiser >= 75 and randomiser < 100:
            # 0.24% chance of sleeping between 5 and 31 seconds
            time.sleep(random.uniform(5, 31))
        else:
            # most of time just randomise a little bit
            time.sleep(random.uniform(delay - 0.25, delay + 0.25))



    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                self.randomise(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    pass

with Listener(on_press=on_press) as listener:
    listener.join()
