import pyautogui
from dotenv import load_dotenv
import os
import time

load_dotenv()
ACC1 = os.getenv("ACC1")
PASS1 = os.getenv("PASS1")

def get_actual_account():
    file = open(os.getenv("ACTUAL_ACCOUNT_PATH"))
    acc = file.read()
    file.close() 
    return acc

def set_actual_account(acc):
    file = open(os.getenv("ACTUAL_ACCOUNT_PATH"), "w")
    file.write(acc)
    file.close() 

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
    time.sleep(0.1)
    set_actual_account(acc)

if __name__ == "__main__":
    pass