import pytube
from pytube.cli import on_progress
import time
import sys
print("")
print("Youtube Video Downloader" + " By")
print('       _________ ____              ____    ____ ___.    \n'
'      /   _____/ |  |__   _____    |  | __ |__| \_ |__  \n'
'      \_____  \  |  |  \  \__  \   |  |/ / |  |  | __ \ \n'
'      /        \ |   Y  \  / __ \_ |    <  |  |  | \_\ \ \n'
'     /_______  / |___|  / (____  / |__|_ \ |__|  |___  /\n'
'             \/      \/        \/       \/           \/ \n')
print ("[+] About script:")
print ("[-] With this script, you can download youtube videos by entering video url.")
print ("[-] Version: 2.0.0")
print ("-------------------")
print ("[+] THIS SCRIPT CODDED BY SHAKIB") 
print ("[-] SITE: www.code-shakib.github.io") 
print ("-------------------")

animation = ["[□□□□□□□□□□] 0%","[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
for i in range(len(animation)):
    time.sleep(0.5)
    sys.stdout.write("\r[+] Loading... " + animation[i % len(animation)])
    sys.stdout.flush() 

url = input('\nEnter video url here: ')
print('[*] Connecting..... ')

try:
    yt = pytube.YouTube(url, on_progress_callback = on_progress)
    print(f'[+] Downloading: {yt.title} ')
    video = yt.streams.get_by_itag(22)
    video.download('D:/Downloads/YouTube Videos')
    print(f'[#] Completed ')
except:  
    print("Some Error!")

print('\n-----------Task Completed!---------------')