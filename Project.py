import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog



def widgets():
    head_label = Label(root, text="YouTube Video Downloader", padx=15, pady=15, font="SegueUI 14", bg="yellow",
                       fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    link_label = Label(root, text="YouTube video link :", bg="pink", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)
    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)
    destination_label = Label(root, text="Destination :", bg="pink", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)
    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)
    search_b = Button(root, text="Search", command=search, width=10, bg="bisque", relief=GROOVE)
    search_b.grid(row=3, column=2, pady=1, padx=1)
    download_b = Button(root, text="Download Video", command=download, width=20, bg="white", pady=10, padx=15,
                        relief=GROOVE, font="Calibre, 15")
    download_b.grid(row=4, column=1, pady=20, padx=20)


def search():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_directory)


def download():
    youtube_link = video_Link.get()
    download_folder = download_Path.get()
    get_video = YouTube(youtube_link)
    video_stream = get_video.streams.first()
    video_stream.download(download_folder)
    messagebox.showinfo("YOUR VIDEO HAS BEEN DOWNLOADED AND SAVED IN\n" + download_folder)


root = tk.Tk()
root.geometry("720x1280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="yellow")
video_Link = StringVar()
download_Path = StringVar()
widgets()
root.mainloop()
