import pyautogui
import time

pyautogui.FAILSAFE = False

last_action_time = {}

cooldowns = {
    "PLAY": 2.0,
    "PAUSE": 2.0,
    "NEXT": 2.5,
    "PREVIOUS": 2.5,

    "VOL_UP": 0,
    "VOL_DOWN": 0
}

def perform_action(action):
    global last_action_time
    current_time = time.time()

    # check cooldown
    if action in last_action_time:
        if current_time - last_action_time[action] < cooldowns[action]:
            return

    if action == "PLAY":
        pyautogui.press("playpause")

    elif action == "PAUSE":
        pyautogui.press("playpause")

    elif action == "NEXT":
        pyautogui.press("nexttrack")

    elif action == "PREVIOUS":
        pyautogui.press("prevtrack")

    elif action == "VOL_UP":
        pyautogui.press("volumeup")

    elif action == "VOL_DOWN":
        pyautogui.press("volumedown")

    last_action_time[action] = current_time
