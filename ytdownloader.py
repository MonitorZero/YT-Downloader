from tkinter import *
from tkinter import ttk
from pytube import YouTube, extract
import pytube
import os


## Tkinter 
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)


## The Video Downloader
def Downloader():     
    destination = os.path.expanduser('~/Videos')
    url =YouTube(str(link.get()))
    video = url.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
    video.download(output_path=destination)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 105 , y = 200)

## The MP3 Downloader
# There's no way to natively download .mp3 files with PyTube so this is a work around
def MP3Downloader():
    destination = os.path.expanduser('~/Music')
    url =YouTube(str(link.get()))
    mp3 = url.streams.filter(only_audio=True).first()
    out_file = mp3.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 268 , y = 200) 

## The Buttons
Button(root,text = 'GET VIDEO', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=120 ,y = 150)
Button(root,text = 'GET MP3', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = MP3Downloader).place(x=270 ,y = 150)

root.mainloop()