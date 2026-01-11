# Gesture-Controlled Virtual Calculator 🖐️🧮

A **touchless, gesture-based virtual calculator** built using **Computer Vision and Human–Computer Interaction (HCI)** principles. The system allows users to perform arithmetic operations in real time using **hand gestures captured via a webcam**, without any physical input devices.

This project prioritizes **intent-driven interaction**, stability, and explainable engineering — not just visual novelty.

---

## 👥 Collaborators

* **Dharmit Kunal Shah** – System architecture, gesture logic, HUD-style UI/UX design, interaction stability, calculator engine
* **Ishaan Chand** – Gesture experimentation, testing, optimization, and interaction refinement

> Built collaboratively with shared responsibility over design decisions, debugging, and interaction behavior.

---

## ✨ Key Features

### 🖐️ Gesture-Based Interaction

* **Pinch (Thumb + Index)** → Press calculator button
* **Swipe Left (Index Finger)** → Backspace
* **Closed Fist (Hold)** → Clear entire expression

All gestures are **edge-triggered** and **time-gated** to prevent accidental or repeated inputs.

---

### 🧠 Intent-Driven Click System

* No hover-based clicking
* No frame-based repetition
* One gesture → one action

The system combines:

* Pinch detection
* Gesture latching
* Temporal thresholds

Result: **high accuracy with near-zero false positives**.

---

### 🖥️ HUD-Style Glassmorphism UI

* Semi-transparent glass buttons
* Visual hover intensity feedback
* Operator color distinction
* Floating display panel

The UI is designed to feel like a **futuristic command interface**, not a traditional calculator.

---

### 🧮 Custom Calculator Engine

* No unsafe `eval()` usage
* Deterministic arithmetic evaluation
* Clean and explainable computation logic

---

### 📊 Performance Awareness

* Real-time FPS monitoring
* Stable interaction across varying frame rates

---

## 🧩 Project Architecture

```
virtual_calculator/
│
├── core/
│   ├── hand_tracker.py     # MediaPipe hand landmark detection
│   ├── gestures.py         # Gesture recognition & intent logic
│   ├── ui.py               # HUD-style UI rendering
│   ├── calculator.py      # Arithmetic evaluation engine
│   └── metrics.py          # FPS and performance tracking
│
├── main.py                 # Application orchestration
├── requirements.txt
└── README.md
```

Each module follows **single-responsibility design**, making the system clean, testable, and extensible.

---

## ⚙️ Technologies Used

* **Python 3.11**
* **OpenCV** – Video capture and rendering
* **MediaPipe** – Real-time hand landmark detection
* **NumPy** – Mathematical operations

---

## 🧪 Interaction Stability Design

Unlike naive gesture projects, this system uses:

* **Edge-triggered gestures** (press fires once per gesture)
* **Temporal gating** (minimum time between actions)
* **Gesture state management**

This ensures predictable, professional-grade interaction behavior.

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python main.py
```

Ensure a webcam is connected and accessible.

---

## 📌 Use Cases

* Touchless interfaces
* Human–Computer Interaction experiments
* Computer vision demonstrations
* Hackathons and technical showcases
* Accessibility-focused interaction systems

---

## 🚀 Future Enhancements

* Scientific calculator mode
* Gesture-only UI (no visible buttons)
* Audio or haptic feedback
* Adaptive gesture calibration

---

## 🧠 Design Philosophy

This project prioritizes:

* **Intent over motion**
* **Stability over speed**
* **Engineering discipline over gimmicks**

The objective was to build a **real interaction system**, not just a visual demo.

---

## 📄 License

Open for learning and experimentation. Attribution is appreciated.

---

**Built with precision, collaboration, and curiosity.**
