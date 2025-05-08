
from pytube import YouTube
from tkinter import messagebox

def download_video(video_url):

    if not video_url.strip():
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(video_url)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        if "ConnectionError" in str(e):
            messagebox.showwarning("Error", "YouTube server is currently unavailable. Please try again later.")
        else:
            messagebox.showwarning("Error", f"An error occurred: {e}")