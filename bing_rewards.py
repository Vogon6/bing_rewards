from time import sleep
import pyautogui

def alttab():
	pyautogui.keyDown('alt')
	pyautogui.press('tab')
	pyautogui.keyUp('alt')

alttab()

for i in range(1,31):
	pyautogui.typewrite('The count says "%d Bing searches, ah ah ah"' %(i))
	pyautogui.press('enter')
	sleep(4)

	pyautogui.keyDown('alt')
	pyautogui.press('left')
	pyautogui.keyUp('alt')
	sleep(4)

alttab()

print 'Search complete, 150 rewards points earned. Spencer is truly a genius.'