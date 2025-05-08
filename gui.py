import tkinter as ttk
from downloader import download_video

def downloader_gui():
    window = ttk.Tk()
    window.title("🎬 YOUTUBE-DOWNLOADER")
    window.config(background= "white")
    window.geometry("500x500")
    window.resizable(False, False)


    # Create GUI elements
    ttk.Label(
                window, text="🎬 YouTube Video Downloader", 
                font=("Segoe UI", 16, "bold"), 
                anchor="center").pack(pady=10)

    ttk.Label(window, text="Enter YouTube URL:", 
            font=("Arial", 12, "bold")).place(relx=0.5, rely=0.3, anchor=ttk.CENTER)

    ttk.Label(window, text="Rules for Using the YouTube Download", 
            font=("Arial", 12, "bold")).place(relx=0.1, rely=0.75, anchor=ttk.W)


    url_entry = ttk.Entry(window, 
                        width=50, 
                        font=("Arial", 12), 
                        relief="groove", 
                        borderwidth=2)
    url_entry.place(relx=0.5, rely=0.4, anchor=ttk.CENTER)

    download_btn = ttk.Button(window, text="Download", 
                            command= lambda: download_video(url_entry.get()), 
                            font=("Arial", 12, "bold"),
                            padx=6,
                            bg="#4CAF50",  # green color
                            fg="white",  # white text color
                            activebackground="#3e8e41",  # darker green on hover
                            activeforeground="white")  # white text color on hover
    download_btn.place(relx=0.5, rely=0.5, anchor=ttk.CENTER)

    rules = [
        "1. Respect YouTube's Terms of Service",
        "2. Do not download copyrighted content",
        "3. Do not share or distribute downloaded videos",
        "4. Use the download for personal, non-commercial purposes only"
    ]

    for i, rule in enumerate(rules):
        ttk.Label(window, text=rule, font=("Arial", 10)).place(relx=0.1, rely=0.8 + (i * 0.05), anchor=ttk.W)

    return window