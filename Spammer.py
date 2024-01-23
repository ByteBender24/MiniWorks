import pyautogui, time

def spam(spam_text = "Get spammed", times = 50):
        try:
            
            time.sleep(5)
            #change the time of delay between code run and spamming start
            
            for i in range(times):
                pyautogui.typewrite(spam_text)  
                pyautogui.press("enter")
                print("Spammed successfully")
        except:
            print("error")

spam(times = 10)
