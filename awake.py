# background_task.py
import time
import pyautogui

def wide_awake(stop_event, seconds):
    try:
        while not stop_event.is_set():
            time.sleep(seconds)
            pyautogui.hotkey("ctrl")
            time.sleep(seconds)
            pyautogui.hotkey("ctrl")
    except KeyboardInterrupt:
        pass
