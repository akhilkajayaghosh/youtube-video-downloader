from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

window=tk.Tk()
window.geometry("800x250")
window.title("Youtube Downloader")
window.configure(bg="#BEBEBE")
window.resizable(False,False)
def download(url,op):
    try:
        yt = YouTube(url)
        yt=yt.streams.get_highest_resolution()
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
l2=tk.Label(window, text="Select Destination Folder",font=(25))
l2.place(x=0,y=100)

op=tk.Entry(window,width=40,font=(40),text=my_dir)
op.place(x=250,y=100)
b2=tk.Button(window, text="Browse",width=8,height=1,command=browse)
b2.place(x=695,y=101)
def getdata():
    global url,op
    download(url.get(),op.get())
b1=tk.Button(window,width=11,height=1,text="DOWNLOAD",font=(25),command=getdata)
b1.configure(bg="darkgreen")
b1.place(x=300,y=150)

window.mainloop()
