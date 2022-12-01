import pyautogui
from dotenv import load_dotenv
import os
import time
import tkinter
import customtkinter

load_dotenv()
ACC1 = os.getenv("ACC1")
PASS1 = os.getenv("PASS1")
ACC2 = os.getenv("ACC2")
PASS2 = os.getenv("PASS2")

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  
app = customtkinter.CTk()  
app.geometry("400x240")
app.title("Choose account")
app.eval("tk::PlaceWindow . center")
button = customtkinter.CTkButton(master=app, text=ACC1, command=lambda: check_account(ACC1, PASS1))
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app, text=ACC2, command=lambda: check_account(ACC2, PASS2))
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


def get_actual_account():
    file = open(os.getenv("ACTUAL_ACCOUNT_PATH"))
    acc = file.read()
    file.close() 
    return acc

def set_actual_account(acc):
    global app
    file = open(os.getenv("ACTUAL_ACCOUNT_PATH"), "w")
    file.write(acc)
    file.close() 
    app.destroy()

def check_account(acc, passwd):
    if acc != get_actual_account():
        os.startfile(os.getenv("SPOTIFY_PATH"))
        time.sleep(3)
        change_account(acc, passwd)

def change_account(acc, passwd):
    time.sleep(0.3)
    pyautogui.moveTo(1650, 30)  #position of account button 
    pyautogui.click()
    pyautogui.moveTo(1650, 250) #position of exit button
    pyautogui.click()
    pyautogui.moveTo(960, 350)  #position of username
    pyautogui.click()
    pyautogui.press('backspace', presses=30)
    time.sleep(0.5)
    pyautogui.write(acc)
    pyautogui.moveTo(960, 420)  #position of password
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(passwd)
    pyautogui.moveTo(960, 550)  #position of access button
    pyautogui.click()
    time.sleep(0.1)
    set_actual_account(acc)

def button_function():
    print("button pressed")

if __name__ == "__main__":
    app.mainloop()