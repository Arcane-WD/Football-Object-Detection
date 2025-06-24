
# ⚽ Football Object Detection & Analysis System

This project is a full-fledged Football Analysis System built using **YOLOv8**, **OpenCV**, **PyTorch**, and **Computer Vision techniques**. It demonstrates real-time **object detection**, **player tracking**, **team assignment**, **camera motion compensation**, **speed and distance estimation**, and **perspective transformation** — all aimed at analyzing football matches intelligently.

> Inspired by the tutorial by [Code In a Jiffy](https://youtu.be/neBZ6huolkg?si=FriMCuD-GnvYV-1a)

---

## 🧠 What You'll Learn

In this project, you'll build an end-to-end sports analytics system. Specifically, you'll learn to:

1. 🧠 Use **Ultralytics YOLOv5** for detecting players, referees, and balls in football videos.
2. 🧪 Train your own YOLO model on custom datasets for better detection accuracy.
3. 🎨 Apply **KMeans clustering** for segmenting player t-shirt colors and assign teams.
4. 🎥 Estimate **camera movement** using **Optical Flow**.
5. 🧭 Implement **Perspective Transformation** to map video coordinates to real-world coordinates.
6. 🏃 Measure each player’s **distance covered and speed** over time using tracking data.

---

## 🚀 Project Structure

```

FOOTBALL\_OBJECTDETECTION/
├── camera\_movement\_estimator/
├── development\_and\_analysis/
├── player\_ball\_assigner/
├── speed\_and\_distance\_estimator/
├── team\_assigner/
├── trackers/
├── training/
├── utils/
├── Videos/
├── view\_transformer/
├── main.py
├── yolo\_inference.py
├── README.md
├── pyproject.toml
└── .gitignore

````

---

## 📦 Installation

> ⚠️ Python 3.12+ is required.

```bash
# Clone the repository
git clone https://github.com/Arcane-WD/football-object-detection.git
cd football-object-detection

# Install dependencies using uv (recommended)
uv venv
uv pip install -r requirements.txt  # or use pyproject.toml
````

If you're not using `uv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 📁 Datasets Used

* 📦 [Kaggle Football Dataset](https://www.kaggle.com/competitions/d...) *(Videos were removed)*
* 📼 [Google Drive Video](https://drive.google.com/file/d/1t6ag...) *(used instead of removed Kaggle videos)*
* 🎯 [Roboflow Football Dataset](https://universe.roboflow.com/roboflow...)

---

## 📊 Core Features

| Feature                         | Description                                          |
| ------------------------------- | ---------------------------------------------------- |
| **YOLOv8 Object Detection**     | Detect players, referees, and the ball in each frame |
| **Custom Model Training**       | Train your own YOLO model using annotated data       |
| **Tracking**                    | Track objects across frames using bounding boxes     |
| **Team Color Clustering**       | Assign teams using KMeans on jersey color            |
| **Ball Possession Detection**   | Assign ball possession to players                    |
| **Camera Motion Estimation**    | Adjust player positions with optical flow            |
| **Perspective Mapping**         | Map pixel positions to meters                        |
| **Speed & Distance Estimation** | Calculate player distance covered and movement speed |

---

## 🕓 Tutorial Timestamps

| Time     | Feature                          |
| -------- | -------------------------------- |
| 00:00    | Introduction                     |
| 01:19    | YOLO Object Detection & Tracking |
| 01:55:30 | Team Color Assignment            |
| 02:32:00 | Ball Interpolation               |
| 03:06:25 | Camera Movement Estimator        |
| 03:41:50 | Perspective Transformer          |
| 04:05:40 | Speed & Distance Estimator       |

> See full video [here](https://youtu.be/neBZ6huolkg?si=FriMCuD-GnvYV-1a)

---

## 📂 Sample Output

Outputs such as tracked videos, player labels, and speed overlays are saved in the `/Outputs` directory.

---

## 🔧 Run the System

```bash
python main.py
```

Ensure your input videos are in the `Videos/` folder.

---

## 🧾 License

This project is for educational and research purposes. Please credit the original author for the tutorial and data sources when reusing.

---

## 🙌 Credits

* [Ultralytics YOLOv5](https://github.com/ultralytics/ultralytics)
* [Code In a Jiffy YouTube Tutorial](https://youtu.be/neBZ6huolkg?si=FriMCuD-GnvYV-1a)
* Roboflow & Kaggle for datasets

---

## 🌟 Star this repository if you found it helpful!

```
