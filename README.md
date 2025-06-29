# NeoTouch: Touchless AI Interaction System

**NeoTouch** is an AI-powered, computer vision-based interface that allows you to control your entire desktop **without touching** your keyboard or mouse. Using only **hand gestures and facial movements**, you can navigate, click, scroll, and zoom 

## 🔥 Features

- ✅ **Touchless Cursor Control** – Move the mouse with your index finger.
- ✅ **Pinch to Click** – Simply pinch your thumb and index finger together to perform a click.
- ✅ **Scroll with Two Fingers** – Use index and middle fingers to scroll content up or down.
- ✅ **Smart Zoom with Face Proximity** – Zoom in when your face moves closer to the screen and auto-reset when you lean back.
- 🚫 No hardware gloves or sensors required – only a webcam.

## 🧠 How It Works

NeoTouch uses:
- **MediaPipe** for real-time hand and face tracking.
- **OpenCV** to process webcam input.
- **PyAutoGUI** for controlling the OS GUI based on interpreted gestures.
- **NumPy & Math** to calculate hand distances and facial positions.

## 🎥 Demo

> 📽️ [Watch the Live Demo Video](https://your-link-here.com)  
> *(Demonstrating real-time gesture-based control)*


## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/nileshgorde04/NeoTouch.git
   cd NeoTouch
2. Install the required Python libraries :
   pip install opencv-python mediapipe pyautogui numpy

3. Run Python File
   python neotouch.py


## Controls Guide 

Gesture/Action	Effect
✋ Index Finger Movement	Move the mouse cursor
👌 Pinch Gesture (Thumb + Index)	Perform a mouse click
✌️ Two-Finger Up/Down	Scroll the page vertically
🧑‍🦱 Move Face Closer	Zoom In (Ctrl + +)
🧑‍🦱 Lean Back to Neutral	Zoom Reset (Ctrl + 0)
