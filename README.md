# AI Hand-Controlled Music 🎵🤖

AI Hand-Controlled Music is a touch-free music control system that allows users to control music playback using hand gestures detected through a webcam. The system uses real-time computer vision to recognize gestures and perform actions such as play, pause, changing tracks, and adjusting volume on the Spotify desktop application.

In addition to gesture-based control, the system integrates Generative AI using Google Gemini to generate intelligent responses and music suggestions based on user gestures, creating a more interactive and engaging user experience.

---

## Features

* 🎥 Real-time hand gesture detection using webcam
* ✋ Gesture-based control for music playback
* 🎵 Control Spotify desktop application
* 🤖 Generative AI responses using Google Gemini
* ⚡ Low latency with frame skipping and gesture stabilization
* 🔐 Secure API key management using environment variables

---

## Technologies Used

* **Python** – Core programming language
* **OpenCV** – Real-time video capture and processing
* **MediaPipe** – Hand landmark detection and gesture recognition
* **Google Gemini API** – Generative AI responses
* **PyAutoGUI** – System-level media control for Spotify
* **Spotify Desktop Application** – Music playback platform

These technologies work together to enable real-time gesture recognition and intelligent interaction. 

---

## System Architecture

The system is divided into four main layers:

1. **Presentation Layer** – Displays webcam feed and gesture feedback using OpenCV
2. **Gesture Processing Layer** – Detects hand landmarks using MediaPipe
3. **Decision Layer** – Interprets gestures and generates AI responses using Gemini
4. **Execution Layer** – Sends media commands to Spotify using PyAutoGUI

This modular design ensures real-time performance and easy scalability. 

---

## Supported Gestures

| Gesture       | Action         |
| ------------- | -------------- |
| Closed Fist   | Pause Music    |
| One Finger    | Next Track     |
| Two Fingers   | Previous Track |
| Three Fingers | Volume Up      |
| Four Fingers  | Volume Down    |
| Open Palm     | Play Music     |

Testing confirmed that gestures were detected reliably with immediate response in Spotify. 

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rohibi930/ai-hand-controlled-music.git
cd ai-hand-controlled-music
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

Create an environment variable for the Gemini API key:

```bash
export GEMINI_API_KEY=your_api_key
```

### 4. Run the project

```bash
python main.py
```

---

## Hardware Requirements

Minimum requirements:

* Intel Core i3 processor
* 4 GB RAM
* Webcam
* Internet connection
* Speakers or headphones

A webcam is essential because the system relies on real-time video input for gesture detection. 

---

## Future Improvements

* Add more gesture commands
* Support multiple music platforms
* Improve gesture recognition accuracy
* Mobile or web-based interface

---

## Project Goal

The goal of this project is to demonstrate how **Computer Vision, Human–Computer Interaction, and Generative AI** can be combined to create an intuitive, intelligent, and contactless music control system. 
