# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 00:44:36 2020

@author: Manali
"""

import os
import pyttsx3 as s
s.speak("Welcome i am jack may i help you")
 
    #os.system(q)
while True:
    q = input("enter your choice : ")  
    if (("run" in q) or ("execute" in q) or ("open" in q)) and (("notepad" in q) or ("editor" in q) or ("text editor" in q)):
        s.speak("Notepad Opened")
        os.system("notepad")
    elif (("run" in q) or ("execute" in q) or ("open" in q)) and (("chrome" in q) or ("browser" in q) or ("search engine" in q)):
        s.speak("chrome Opened")
        os.system("chrome")
    elif (("run" in q) or ("play" in q) or ("open" in q)) and (("wm player" in q) or ("windows player" in q)):
        s.speak("windows player Opened")
        os.system("wmplayer")
    elif (("run" in q) or ("play" in q) or ("open" in q)) and (("saavn songs" in q) or ("jio saavn" in q)):
        s.speak("jio saavan Opened")
        os.system("chrome https://www.jiosaavn.com/")
    elif (("run" in q) or ("play" in q) or ("open" in q)) and (("gaana" in q) or ("songs" in q) or ("gaana player" in q) or ("gaana.com" in q)):
        s.speak("music player Opened")
        os.system("chrome https://gaana.com/")
    elif (("run" in q) or ("execute" in q) or ("open" in q)) and (("whatsapp" in q) or ("chat" in q)):
        s.speak("whatsapp Opened")
        os.system("chrome https://web.whatsapp.com/")
    elif (("run" in q) or ("execute" in q) or ("open" in q)) and (("email" in q) or ("mail" in q) or ("gmail" in q)):
        s.speak("mail Opened")
        os.system("chrome https://mail.google.com/mail/")
    elif (("run" in q) or ("execute" in q) or ("open" in q)) and (("aws" in q) or ("aws console" in q) or ("aws cloud" in q)):
        s.speak("aws cloud Opened")
        os.system("chrome aws.amazon.com/console/")
    elif (("run" in q) or ("execute" in q) or ("open" in q)) and (("gcp" in q) or ("google cloud" in q) or ("gcloud" in q)):
        s.speak("gcp Opened")
        os.system("chrome https://cloud.google.com/")        
    elif (("quit" in q) or ("close" in q) or ("shut down" in q) or ("bye" in q) or ("bye bye" in q) or ("exit" in q)):
        s.speak("Thank You")
        break
    else:
        s.speak("Sorry dear this is not supported")
