# 🎧 Voice Encoder / Decoder (Audio ⇄ Base64)

A simple **audio-to-text and text-to-audio** tool that converts **audio files into Base64 encoded secret codes** and decodes them back into playable audio.

This project includes:
- 🐍 **Python CLI Encoder & Decoder**
- 🌐 **Browser-based Encoder & Decoder (HTML + JavaScript)**
- 🔒 Fully **offline**, no uploads, no server required

---

## 📖 Description

**Voice Encoder / Decoder** transforms any audio file (`.mp3`, `.wav`, etc.) into a **Base64 string**, allowing audio to be stored, shared, or transferred as text.

The encoded text can later be decoded back into the **exact original audio** without any quality loss.

This is **encoding, not encryption** — the goal is data transformation, not security.

---

## ✨ Features

- 🔐 Encode audio files into Base64 text
- 🔊 Decode Base64 text back into audio
- 🧠 Lossless conversion (raw bytes ⇄ Base64)
- 🌐 Browser version works 100% offline
- 🐍 Python version uses only standard libraries
- 📦 No dependencies
- 🎧 Supports all common audio formats

---

## 📁 Project Structure

Voice-Encoder-Decoder



├── encorder.py # Audio → Base64 encoder (Python)


├── decorder.py # Base64 → Audio decoder (Python)


├── index.html # Browser-based UI (offline)


└── README.md # Documentation


---

## 🔧 Requirements

### Python
- Python **3.10 or newer**

### Libraries
No external libraries required.  
Uses only:
- `base64`
- `pathlib`

---

## 🐍 Python Usage (Command Line)

### ▶ Encode Audio to Base64

`Run Index.html`




`🧠 How It Works`
Encoding Process

Audio File → Raw Bytes → Base64 Encoding → Text Code

Decoding Process
Base64 Text → Decode → Raw Bytes → Audio File


Base64 encoding is lossless, meaning:

Audio quality remains unchanged

File size increases by ~33%
