import pyautogui
import time
import string
import pyscreeze
from AutoGUIMod import Action
import os
import datetime
import pathlib
import traceback


Sendto =["Me Mumbai"] # insert name of recipients as a form of list , seprated

Act = Action.Action()
#timeStamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I-%M%p")
AttachmentPath = str(pathlib.Path('.').absolute() / 'SendImg')
objWhatsapppath = str(pathlib.Path('.').absolute() / 'Image' / 'Whatsapp')

TexttoSend = "Testing in progress- Ignore the message"
Act.runOpenApp("chrome")
try:
    if(Act.activeWinName("New Tab - Google Chrome")):
        pyautogui.write("https://web.whatsapp.com/")
        pyautogui.hotkey("enter")
        Act.waitTillImgDisplay(objWhatsapppath +"LoadImg.PNG") #Step not working as expected need to check
        for Recipient in Sendto:
            if(Act.activeWinName("WhatsApp")):
                Act.waitUntilImgDispay(objWhatsapppath + '/txt_Searchorstartnewchat.PNG')
                Act.writeOnImg(objWhatsapppath + '/txt_Searchorstartnewchat.PNG', Recipient)
                time.sleep(3)
                pyautogui.press("enter")
                time.sleep(3)
                Act.clickImage(objWhatsapppath + "/btn_attachment.PNG")
                time.sleep(3)
                Act.waitUntilImgDispay(objWhatsapppath + "/btn_attachimg.PNG")
                Act.clickImage(objWhatsapppath + "/btn_attachimg.PNG")
                time.sleep(5)
                Act.writeOnImg(objWhatsapppath + "/Brows_Attachmentpath.PNG", AttachmentPath)
                pyautogui.press("enter")
                time.sleep(3)
                screenWidth, screenHeight = pyautogui.size()
                pyautogui.click((screenWidth/2),(screenHeight/2))
                pyautogui.keyDown('ctrl')
                pyautogui.press('a')
                pyautogui.keyUp('ctrl')
                pyautogui.press("enter")
                time.sleep(3)
                pyautogui.write(TexttoSend)
                time.sleep(3)
                pyautogui.press("enter")            
        else:
            print("Fail to load the whatsapp window")
except Exception:
    print("Exception ocured")
    traceback.print_exc()
else:
    pyautogui.alert('Execution Completed', "Status")