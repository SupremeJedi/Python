import pyautogui as pt
import time

limit = 25
message = 'hello'
i = 0
time.sleep(1)
no = 1
while i < limit:
    pt.typewrite(message +" "+ str(no) + "x")
    pt.press("enter")
    i = i+1
    no+=1   











    
