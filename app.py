import webbrowser
import pyttsx3 as p
import os
p.speak("Hello! How may I help you today? ")
print(" Enter any of the given options or type in your requirements \n 1.Music \n 2.Coding platform \n 3.Web \n 4.Email \n 5.Game \n 6.Notepad \n 7.Media Player \n 8.Entertainment \n 9.Video call")
while True:
   print("Type in your choice or your requirements!",end=' ')
   s=input()
   if(("Music" in s) or ("music" in s) or ("songs" in s) or ("song" in s) or s=='1'):
          os.system("start spotify:") 
   elif(("Code" in s) or ("code" in s) or ("coding" in s) or ("coding platform" in s) or s=='2'):
          os.system("CodeBlocks")
   elif(("Web" in s) or ("Browser" in s) or ("web" in s) or ("browser" in s) or  s=='3'):
          p=input("Enter the website you want to visit")
          webbrowser.open_new_tab(p) 
   elif(("email" in s) or("mail" in s) or s=='4'):
                if(("email" in s) or("mail" in s) or s=='4'):
                   d=input("Do you want to compose a mail?Enter yes to proceed else enter anything")
                if("Yes" in d or "yes" in d):
                    os.system(" Chrome mail.google.com/mail/u/0/#inbox?compose=new")
                else:
                   os.system("Chrome gmail.com")
   elif(("Game" in s) or ("play" in s) or ("game" in s)  or s=='5'):
          os.system("start Steam:")
   elif(("Notepad" in s) or ("editor" in s) or ("notepad" in s) or s=='6'):
          os.system("Notepad")
   elif(("media player" in s) or ("media" in s) or ("player" in s) or s=='7'):
          os.system("start vlc")
   elif(("watch" in s) or ("shows" in s) or ("movies" in s) or s=='8'):
          os.system("start MOVIES")
   elif(("video" in s) or ("conference" in s) or ("connect" in s) or ("calling" in s) or (s=='9')):
          os.system("start Zoom")
   elif(('exit' in s) or ('leave' in s) or ('quit' in s)):
          p.speak('Thankyou see you soon')
          break
   else:
          print("Invalid input")

else:
  exit()
