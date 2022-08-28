import speedtest
from tkinter import *


test=speedtest.Speedtest()
test.get_servers()  #returns the available servers
best=test.get_best_server() #finds the best server
print("Server Found:",best)

download_speed=test.download() #finds the download speed
upload_speed=test.upload()      #finds the upload speed
ping_speed=test.results.ping     #finds the ping speed
print(download_speed)
print(upload_speed)
print(ping_speed)
window=Tk()   #creates a UI window on the screen 

text=Label(window, text=f"Download speed: {download_speed/1024/1024: 0.2f} mbit/s", fg='red', font=("Helvetica", 16))
text.place(x=60, y=10)
text=Label(window, text=f"upload speed: {upload_speed/1024/1024: 0.2f} mbit/s", fg='red', font=("Helvetica", 16))
text.place(x=60, y=40)

text=Label(window, text=f"ping speed: {ping_speed/1024/1024: 0.2f} ms", fg='red', font=("Helvetica", 16))
text.place(x=60, y=70)


window.geometry("300x200")  #set the geometry of the window, can be changed as per requirement
window.title("SpeedNet")      #set the Title of the window, can be changed as per requirementf
window.mainloop()
