# 🎵 yt-dlp Python Batch MP3 Downloader

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)
![Homebrew](https://img.shields.io/badge/Homebrew-required-orange.svg)
![yt-dlp](https://img.shields.io/badge/Powered%20by-yt--dlp-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A lightweight Python script that automates downloading **MP3 audio** from a list of YouTube URLs using **yt-dlp** and **FFmpeg**.

Simply place your YouTube links in `links.txt`, run the script, and it will:

* 🎵 Download the best available audio
* 🎧 Convert it to MP3
* 📝 Remove each processed URL from `links.txt`
* 🔁 Resume easily if interrupted
* 📂 Save everything in the script folder

---

## ✨ Features

* ✅ Batch download from a text file
* ✅ Automatic MP3 conversion
* ✅ Best available audio quality
* ✅ Automatically skips already downloaded videos
* ✅ Removes completed URLs from the list
* ✅ Resume downloads after interruptions
* ✅ No Python dependencies required

---

## 📦 Requirements

* Python 3
* Homebrew (macOS)
* yt-dlp
* FFmpeg

---

## 🚀 Installation

Install the required tools:

```bash
brew install yt-dlp
brew install ffmpeg
```

Verify the installation:

```bash
yt-dlp --version
ffmpeg -version
ffprobe -version
```

---

## 📁 Project Structure

```text
.
├── download.py
├── links.txt
├── downloaded.txt      # Created automatically
└── *.mp3               # Downloaded audio files
```

---

## 📝 Preparing the Playlist

Create a `links.txt` file with one YouTube URL per line.

Example:

```text
https://www.youtube.com/watch?v=eTPt5ZT7JY0
https://youtu.be/XXXXXXXXXXX
https://www.youtube.com/watch?v=YYYYYYYYYYY
```

---

## ▶️ Usage

Run:

```bash
python3 download.py
```

The script will:

1. Read the first URL
2. Download the audio
3. Convert it to MP3
4. Save the file
5. Remove the URL from `links.txt`
6. Continue until the list is empty

If a download fails, the URL remains in the file so you can retry later.

---


## ⚙️ How It Works

```text
links.txt
     │
     ▼
 Read first URL
     │
     ▼
 Download audio
     │
     ▼
 Convert to MP3
     │
     ▼
 Save file
     │
     ▼
 Remove URL from links.txt
     │
     ▼
 Repeat
```

---

## ❤️ Credits

This project is only a small automation wrapper around the fantastic **yt-dlp** project.

**yt-dlp Official Repository**

https://github.com/yt-dlp/yt-dlp

If you find this project useful, please consider giving ⭐ to the original repository.

---

## 📄 License

This project is released under the MIT License.

The downloading engine is provided by **yt-dlp**, which is maintained by its respective contributors.
