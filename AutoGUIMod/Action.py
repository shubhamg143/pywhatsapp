import pyautogui
import time
import string
import datetime

class Action:
    def __init__(self):
        print("")

    def runOpenApp(self, Texttoenter: str):
        pyautogui.hotkey("win", "r")
        time.sleep(2)
        pyautogui.write(Texttoenter)
        pyautogui.hotkey("enter")
        time.sleep(5)

    def clickImage(self, imgpath: str):
        try:
            buttonlocation = pyautogui.locateOnScreen(imgpath, confidence=0.9)
            if buttonlocation == None:
                pyautogui.screenshot("Screenshot//clickImg_.png")
                print("Fail to click -Image not found on screen")
            else:
                pyautogui.click(pyautogui.center(buttonlocation))
                # pyautogui.click(imgpath)
                print("Image has been clicked")
        except Exception as e:
            print(e + " Error occur to click the image")

    def doubleClkImg(self, imgpath: str):
        try:
            pyautogui.doubleClick(imgpath)
            print("Image has been clicked")
        except Exception as e:
            print(e + " Error occur to click the image")

    def clickImgConf(self, imgpath: str, conf):
        buttonlocation = pyautogui.locateOnScreen(imgpath, confidence=conf)
        if buttonlocation == None:
            pyautogui.screenshot("Screenshot//Image.png")
            print("Fail to click -Image not found on screen")
        else:
            x, y = pyautogui.center(buttonlocation)
            pyautogui.click(x, y)

    def writeOnImg(self, imgpath: str, txt: str):
        self.clickImgConf(imgpath, 0.8)
        pyautogui.write(txt)

    def activeWinName(self, WinTitle: str):
        ActiveWindow: str = pyautogui.getActiveWindowTitle()
        try:
            if WinTitle in ActiveWindow:
                print(WinTitle + " is active window")
                return True
            else:
                print(WinTitle + " is not active window" + "-" + ActiveWindow)
                return False
        except Exception as e:
            print("Exception occured- ")
            print(e)
# waitTillImgDisplay - not working as expected, comes out with in 0 Sec each time.

    def waitTillImgDisplay(self, imgpath: str):
        waitcount = 0
        while(True):
            try:
                buttonlocation = pyautogui.locateOnScreen(
                    imgpath, confidence=0.9)
                if(buttonlocation == None):
                    print("Image time on screen " + str(waitcount*2) + " Sec")
                    break
            except:
                print("Exception occured-")
                print(Exception)
                break
            else:
                print()
                waitcount = waitcount + 1
                if waitcount <= 30:
                    time.sleep(2)
                    continue
                else:
                    print("60 sec wait time over- Image still present on screen")
                    pyautogui.screenshot(
                        "Screenshot//waitTillImgDisplayError.png")
                    break

    def waitUntilImgDispay(self, imgpath: str):
        waitcount = 0
        while(True):
            try:
                buttonlocation = pyautogui.locateOnScreen(
                    imgpath, confidence=0.9)
                if(buttonlocation != None):
                    print("wait time over in " + str(waitcount*2) + " Sec")
                    break
            except Exception as e:
                print(e)
                break

            else:
                waitcount = waitcount + 1
                if waitcount <= 30:
                    time.sleep(2)
                    continue
                else:
                    print("60 sec wait time over- Image not founnd on screen")
                    break
                print("Image display wait time over in " + waitcount*2 + "Sec")
                break

    def selectActiveWinByTitle(self, SearchWinTitle: str):
        i = 0
        FoundFlag = 0
        while i < 10:
            i = i+1
            Actwind = pyautogui.getActiveWindow()
            WinTitle = str(Actwind.title)
            if WinTitle.find(SearchWinTitle) == -1:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                time.sleep(2)
                continue
            else:
                FoundFlag = 1
                print("Active window is: " + Actwind.title)
                return True
        if i == 10 and FoundFlag == 0:
            print("Window not found with name: " + SearchWinTitle)
            return False

    def ClickImgRight(self,ImgPath: str):
        buttonlocation = pyautogui.locateOnScreen(ImgPath, confidence=0.9)
        if buttonlocation == None:
            timeStamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I-%M%p")
            pyautogui.screenshot("Screenshot//Image_"+ timeStamp + ".png")
            print("Image not found on screen")
        else:
            x, y = pyautogui.center(buttonlocation)
            x = x + (buttonlocation.width/2)
            x = x+100
            print("clicking on coordiante ", x, " ",y)
            pyautogui.click(x, y)

