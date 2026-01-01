# VoluGesture: AI-Powered Hand Volume Control

**VoluGesture** is a computer vision tool that allows you to control your system's master volume using hand gestures. By measuring the distance between your thumb and index finger, you can "slide" the volume up and down in real-time.

## 🚀 Features

* **Real-time Tracking:** Powered by MediaPipe for high-accuracy hand landmark detection.
* **Visual UI:** Includes an on-screen volume bar and percentage indicator.
* **Dynamic Feedback:** The tracker changes color based on volume levels (Green for Max, Red for Min).
* **Modular Design:** Uses a custom `HandTrack` module that can be reused for other projects.

---

## 🛠️ How it Works

The script calculates the **Euclidean Distance** between the tip of the thumb and the tip of the index finger.

1. **Index Finger Tip:** Landmark #8
2. **Thumb Tip:** Landmark #4
3. **Distance Calculation:** Using `np.hypot(x2-x1, y2-y1)`

The distance is then mapped from pixels to the system's decibel range (via `pycaw`) using linear interpolation.

---

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/VoluGesture.git
cd VoluGesture

```


2. **Install dependencies:**
```bash
pip install opencv-python mediapipe numpy pycaw

```


3. **Run the application:**
```bash
python main.py

```



---

## 📂 Project Structure

* `main.py`: The entry point for the volume control application.
* `HandTrack.py`: A reusable class for hand detection and landmark positioning.
* `README.md`: Project documentation.

---

## 🎮 Usage

1. Run the script and wait for the webcam window to open.
2. Show your **Right Hand** to the camera.
3. Bring your **Thumb** and **Index** finger together to lower the volume.
4. Spread them apart to increase the volume.
5. Press **Esc** to exit the program.

---

## 📝 Requirements

* Python 3.x
* Webcam
* Windows OS (Required for `pycaw`)

---

## 🤝 Contributing

Feel free to fork this project and add features! I'm planning to add more gestures for different system controls (like brightness or media play/pause) soon.

---

### Would you like me to help you write a similar README for your Subway Surfers gesture project?