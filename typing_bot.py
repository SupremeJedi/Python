import time
import pyautogui


time.sleep(4)
text = open("text.txt")
for each_line in text:
    pyautogui.typewrite(each_line)