# 🏃‍♂️ SubFers-Vision

**Transforming Hand Kinetics into Digital Motion.**

**SubFers-Vision** is a gesture-based game controller built with Computer Vision. It allows you to play "Subway Surfers" (and other infinite runner games) by using your hands in thin air. No keyboard, no mouse—just motion.

## 🌟 The Journey

This project started with a spark of inspiration. During my **Freshman year**, I saw a creator on TikTok build a gesture-controlled game. I promised myself I would learn how it worked. During my **Sophomore Christmas break**, I dived deep into Computer Vision and Python to turn that inspiration into reality.

**SubFers-Vision** is the result: a bridge between physics and gaming.

---

## 🛠️ How it Works

The project is split into a modular architecture for high performance and reusability:

* **`GestureCore.py`**: The "Brain." It handles the camera feed, processes RGB frames through MediaPipe, and extracts a 21-point landmark list with specific (x, y) coordinates.
* **`VisionController.py`**: The "Translator." It takes the raw landmark data and maps specific finger configurations to `pyautogui` keyboard events.

### 🎮 Controls

| Action | Gesture | Physics Logic |
| --- | --- | --- |
| **JUMP** | Open Palm 🖐️ | All finger tips (8, 12, 16, 20) are above their bases. |
| **ROLL** | Closed Fist ✊ | All finger tips are below their mid-joints. |
| **LEFT** | Two Fingers ✌️ | Index and Middle fingers detected as "Up." |
| **RIGHT** | One Finger ☝️ | Only Index finger detected as "Up." |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* A webcam

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/SubFers-Vision.git
cd SubFers-Vision

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Launch the game:**
Open Subway Surfers in your browser or a Windows app, then run the controller:
```bash
python VisionController.py

```



---

## 🗺️ Roadmap

* [x] Initial Hand Tracking Engine (`GestureCore`)
* [x] Basic Key Mapping (Up, Down, Left, Right)
* [ ] Multi-hand support for power-ups
* [ ] Geometry Dash "One-Tap" Mode integration
* [ ] Sensitivity calibration UI

