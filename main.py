import pyautogui
from dotenv import load_dotenv
import os

load_dotenv()
ACC1 = os.getenv("ACC1")
PASS1 = os.getenv("PASS1")


pyautogui.moveTo(1650, 30)  #position of account button