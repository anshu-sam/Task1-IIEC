
#!/usr/bin/env python
import webbrowser
import getpass as g
import pyttsx3 as f
import time
import os
f.speak("Hello! How may I help you today? ")
print(" Enter any of the given options or type in your requirements \n 1.Music \n 2.Coding platform \n 3.Web \n 4.Email \n 5.Game \n 6.Notepad \n 7.Media Player \n 8.Movies \n 9.Video call")
while True:
   print("Type in your choice or your requirements!",end=' ')
   s=input()
   if(("Music" in s) or ("music" in s) or ("songs" in s) or ("song" in s) or s=='1'):
          os.system("start spotify:") 
          print("               Spotify launched               ")
          print("\n")                              
   elif(("Code" in s) or ("code" in s) or ("coding" in s) or ("coding platform" in s) or s=='2'):
          os.system("CodeBlocks")
          print("               Codeblocks launched               ")
          print("\n")   
   elif(("Web" in s) or ("Browser" in s) or ("web" in s) or ("browser" in s) or  s=='3'):
          p=input("Enter the website you want to visit")
          webbrowser.open_new_tab(p) 
          print("               Web launched               ")
          print("\n")   
   elif("joke" in s or "Joke" in s):
          f.speak('What do you call a bee that cant make up its mind?')
          time.sleep(7)
          f.speak('A         maybe')
          f.speak("Opening a website to entertain you")
          os.system("Chrome www.boredpanda.com/funny-pun-jokes")
   elif(("email" in s) or("mail" in s) or s=='4'):
           d=input("Do you want to compose a mail?Enter yes to proceed else enter anything")
           if("Yes" in d or "yes" in d):
               import smtplib

               from email.mime.text import MIMEText

               port = 587
               sender = 'anshusam123@outlook.com'
               receiver = input('Enter mail id of who you want to send to!')
               msg = MIMEText(input('Enter your message'))

               msg['Subject'] = input('Enter subject')
               msg['From'] = 'anshusam123@outlook.com'
               msg['To'] =  'anshusam123@gmail.com'

               user = 'anshusam123@outlook.com'
               password = g.getpass('Enter your password')

               with smtplib.SMTP("smtp.outlook.com", port) as server:

                   server.starttls() # Secure the connection
                   server.login(user, password)
                   server.sendmail(sender, receiver, msg.as_string())
                   print("mail successfully sent")
	
           else:
                os.system("Chrome gmail.com") 
           print("               Mail launched               ")
           print("\n")   
   elif(("Game" in s) or ("play" in s) or ("game" in s)  or s=='5'):
          os.system("start Steam:")
          print("               Game launched               ")
          print("\n")   
   elif(("Notepad" in s) or ("editor" in s) or ("notepad" in s) or s=='6'):
          os.system("Notepad")
          print("               Notepad launched               ")
          print("\n")   
   elif(("media player" in s) or ("media" in s) or ("player" in s) or s=='7'):
          os.system("start vlc")
          print("               VLC launched               ")
          print("\n")   
   elif(("watch" in s) or ("shows" in s) or ("movies" in s) or s=='8'):
          os.system("start MOVIES")
          print("               Movies shown              ")
          print("\n")   
   elif(("video" in s) or ("conference" in s) or ("connect" in s) or ("calling" in s) or (s=='9')):
          os.system("start Zoom")
          print("               Zoom succesfully opened               ")
          print("\n")   
   elif(('exit' in s) or ('leave' in s) or ('quit' in s)):
          f.speak('Thankyou!   see you soon')
          break
   else:
          print("Invalid input")

else:
  exit()
