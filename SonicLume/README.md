# SonicLume 🖐️🔊💡

**SonicLume** is an AI-powered system controller that transforms your hand gestures into hardware commands. Using Computer Vision, it maps the distance between your fingertips to system levels, allowing for a touchless "slider" experience.

## 🛠️ Current Functionality

The project uses a **Dual-Hand Logic** system to separate audio and visual controls:

| Hand | Control Type | Status | Gesture |
| --- | --- | --- | --- |
| **Right Hand** | **System Volume** | ✅ Functional | Thumb-Index Pinch (Landmarks 4 & 8) |
| **Left Hand** | **Screen Brightness** | 🚧 Coming Soon | Thumb-Index Pinch (Landmarks 4 & 8) |

---

## 🚀 How It Works

1. **Detection:** The system uses `MediaPipe` to detect hand landmarks and identify "Handedness" (Left vs. Right).
2. **Measurement:** It calculates the Euclidean distance () between the thumb tip and index tip.
3. **Mapping:** This distance is interpolated to match system ranges:
* **Volume:** Mapped to decibel levels using `pycaw`.
* **Brightness:** Mapped to percentage (0-100%).



---

## 📂 Project Structure

* `HandTrack.py`: A modular class that handles camera input, RGB conversion, and landmark extraction.
* `main.py`: The main loop that processes the **Right Hand** logic for Volume control.
* `requirements.txt`: List of necessary Python libraries.

---

## 🔧 Installation & Setup

1. **Clone the repo:**
```bash
git clone https://github.com/yourusername/SonicLume.git

```


2. **Install dependencies:**
```bash
pip install opencv-python mediapipe numpy pycaw

```


3. **Run the script:**
```bash
python main.py

```



---

## 🗺️ Roadmap

* [x] High-accuracy hand tracking module.
* [x] Right-hand Volume control integration.
* [ ] Left-hand Brightness control integration (Planned).
* [ ] Visual toggle for "Mute" using a fist gesture.
* [ ] Support for dual-monitor brightness.

---

### Pro-Tip for your GitHub:

Since you mentioned the brightness is "to be implemented," you can leave a comment in your `main.py` code like this:

```python
# TODO: Implement Left Hand detection for Brightness
# if label == "Left":
#     brightness_val = np.interp(length, [35, 210], [0, 100])
#     sbc.set_brightness(int(brightness_val))

```
