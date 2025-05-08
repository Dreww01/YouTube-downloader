# YouTube Video Downloader (Tkinter GUI)

A Python-based YouTube video downloader with a graphical user interface (GUI) built using `Tkinter`. This application allows users to download YouTube videos in MP4 format by simply entering the video URL.

## Features

- User-friendly GUI for downloading YouTube videos.
- Downloads videos in MP4 format with progressive streams.
- Displays rules for ethical usage of the downloader.
- Error handling for invalid URLs or connection issues.

## Requirements

- Python 3.x
- Libraries:
  - `pytube`
  - `tkinter` (comes pre-installed with Python)

## Installation

1. Clone or download this repository.
2. Install the required library:
   ```bash
   pip install pytube
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
   file to launch thr GUI application.
2. Enter the YouTube video URL in the input field.
3. Click the "Download" button to start downloading the video.
4. The downloaded video will be saved in the current working directory.

## Rules for Using the Downloader

1. Respect YouTube's Terms of Service.
2. Do not download copyrighted content.
3. Do not share or distribute downloaded videos.
4. Use the downloader for personal, non-commercial purposes only.

## Example

1. Launch the application.
2. Enter a valid YouTube URL (e.g., `https://www.youtube.com/watch?v=example`).
3. Click "Download" and wait for the success message.


## Notes

- Ensure that the `pytube` library is installed before running the script.

## Troubleshooting

- If you encounter any errors, please check the console output for more information.
- Make sure you have the latest version of pytube installed.
-  If you encounter issues with `pytube`, try upgrading it:
  ```bash
  pip install --upgrade pytube
  ```

## License

This project is open source and available under the MIT License.

## Disclaimer

This script is provided as-is, without warranty of any kind. Use it at your own risk. Please adhere to YouTube's terms of service and copyright laws.
