
import pyautogui
import keyboard
import time


speedz = .45


#time.sleep(5)


# Push shift and t  to start attacking, use right alt to end


## [wastes 100% of cpu when doing if --> ]if keyboard.is_pressed('left alt'):
while True:
    keyboard.wait('shift+t')
    while (2 > 1):
        pyautogui.click(interval=speedz)
        if keyboard.is_pressed('right alt'):
            break
