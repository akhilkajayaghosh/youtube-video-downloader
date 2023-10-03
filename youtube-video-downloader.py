from pytube import YouTube
import tkinter as tk
from tkinter import OptionMenu, StringVar, filedialog

window=tk.Tk()
window.geometry("800x350")
window.title("Youtube Downloader")
window.configure(bg="#BEBEBE")
window.resizable(False,False)

def display_selected(choice):
    global menu2
    lt=tk.Label(window, text="Format",font=(25),width=10)
    lt.place(x=300,y=130)
    menu2=StringVar()
    menu2.set("select")
    format=[]
    choice = menu1.get()
    for i in yt.streams.filter(type="video",res=choice,progressive=True):
        format.append(i.mime_type)
    format=(list(set(format)))
    drop= OptionMenu(window, menu2,*format)
    drop.place(x=420,y=130)    

def getdetails():
    global yt,menu1
    lr=tk.Label(window, text="Resolution",font=(25),width=10)
    lr.place(x=300,y=100)
    menu1=StringVar()
    menu1.set("select")
    yt = YouTube(url.get())
    res1=[]
    for i in yt.streams.filter(type="video",progressive=True):
        res1.append(i.resolution)
    res1=(list(set(res1)))
    drop= OptionMenu(window,menu1,*res1,command=display_selected)
    drop.place(x=420,y=100)
    
def download():
    try:
        yt=YouTube(url.get())
        yt=yt.streams.filter(res=menu1.get(),mime_type=menu2.get(),type="video").first()
        yt.download(op.get())
        status.configure(text="Successfully downloaded")
    except:
        status.configure(text="Error!!")

my_dir=''
def browse():
    global op
    my_dir= filedialog.askdirectory()
    op.insert(0,my_dir)
    
l1=tk.Label(window, text="Paste your Video URL",font=(25))
l1.place(x=0,y=50)
url=tk.Entry(window,width=40,font=(40))
url.place(x=250,y=50)
l2=tk.Label(window, text="Select Destination Folder",font=(25))
l2.place(x=0,y=180)
op=tk.Entry(window,width=40,font=(40),text=my_dir)
op.place(x=250,y=180)
b2=tk.Button(window, text="Browse",width=8,height=1,command=browse)
b2.place(x=695,y=180)
b2.configure(bg="#C4AB37")
b3=tk.Button(window, text="Enter",width=8,height=1,command=getdetails)
b3.place(x=695,y=51)
b3.configure(bg="#C4AB37")
status=tk.Label(window, text="",font=(30),bg="#BEBEBE")
status.place(x=300,y=280)   
b1=tk.Button(window,width=11,height=1,text="DOWNLOAD",font=(25),command=download)
b1.configure(bg="darkgreen")
b1.place(x=300,y=230)
window.mainloop()
