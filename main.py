import pyautogui
from dotenv import load_dotenv
import os
import time

load_dotenv()
ACC1 = os.getenv("ACC1")
PASS1 = os.getenv("PASS1")


def open_spotify():
    os.startfile(os.getenv("SPOTIFY_PATH"))

def change_account(acc, passwd):
    time.sleep(0.3)
    pyautogui.moveTo(1650, 30)  #position of account button 
    pyautogui.click()
    pyautogui.moveTo(1650, 250) #position of exit button
    pyautogui.click()
    pyautogui.moveTo(960, 350)  #position of username
    pyautogui.click()
    pyautogui.press('backspace', presses=20)
    time.sleep(0.1)
    pyautogui.write(acc)
    pyautogui.moveTo(960, 420)  #position of password
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(passwd)
    pyautogui.moveTo(960, 550)  #position of access button
    pyautogui.click()

if __name__ == "__main__":
    open_spotify()
    time.sleep(5)
    #change_account(ACC1, PASS1)
