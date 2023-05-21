from pytube import YouTube
import tkinter as tk
from tkinter import OptionMenu, StringVar, filedialog

window=tk.Tk()
window.geometry("800x350")
window.title("Youtube Downloader")
window.configure(bg="#BEBEBE")
window.resizable(False,False)
lr=tk.Label(window, text="Resolution",font=(25),width=10).place(x=300,y=100)
lt=tk.Label(window, text="Type",font=(25),width=10).place(x=300,y=130)
menu1=StringVar()
menu2=StringVar()
menu1.set("select")
drop= OptionMenu(window, menu1,"select")
drop.place(x=418,y=100)
drop= OptionMenu(window, menu2,"select")
drop.place(x=418,y=130)
menu2.set("select")
global yt,rs1,format

def getdetails(url):
    yt = YouTube(url)
    res1=[]
    format=[]
    for i in yt.streams.filter(type='video'):
        res1.append(i.resolution)
        format.append(i.mime_type)
    res1=(list(set(res1)))
    format=(list(set(format)))
    drop= OptionMenu(window, menu1,*res1)
    drop.place(x=420,y=100)
    drop= OptionMenu(window, menu2,*format)
    drop.place(x=420,y=130)
    
def download(url,op):
    try:
        yt=YouTube(url)        
        yt=yt.streams.filter(res=menu1.get(),mime_type=menu2.get(),type='video').first()
        yt.download(op)
        tk.messagebox.showinfo("showinfo", "Downloaded Successfully")
    except:
        tk.messagebox.showerror("showerror", "Error")
        
my_dir=''

def browse():
    global op
    my_dir= filedialog.askdirectory()
    op.insert(0,my_dir)
    
l1=tk.Label(window, text="Paste your Video URL",font=(25))
l1.place(x=0,y=50)
url=tk.Entry(window,width=40,font=(40))
url.place(x=250,y=50)

def getdata():
    global url
    getdetails(url.get())
  
l2=tk.Label(window, text="Select Destination Folder",font=(25))
l2.place(x=0,y=180)
op=tk.Entry(window,width=40,font=(40),text=my_dir)
op.place(x=250,y=180)
b2=tk.Button(window, text="Browse",width=8,height=1,command=browse)
b2.place(x=695,y=180)
b2.configure(bg="#C4AB37")
b3=tk.Button(window, text="Check",width=8,height=1,command=getdata)
b3.place(x=695,y=51)
b3.configure(bg="#C4AB37")

def start():
    getdetails(url.get())
    download(url.get(),op.get()) 
    
b1=tk.Button(window,width=11,height=1,text="DOWNLOAD",font=(25),command=start)
b1.configure(bg="darkgreen")
b1.place(x=300,y=230)
window.mainloop()
