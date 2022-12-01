import pyautogui
from dotenv import load_dotenv
import os

load_dotenv()
print(pyautogui.size())

ACC1 = os.getenv("ACC1")
PASS1 = os.getenv("PASS1")

print(ACC1, PASS1)