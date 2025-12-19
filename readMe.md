# CrowdCounter

CrowdCounter is a Python-based computer vision project designed for detecting and counting individuals in crowded environments. It utilizes the **YOLOv11** (You Only Look Once) architecture for high-speed, accurate object detection and includes a comprehensive suite of data augmentation tools to improve model robustness.

## 🚀 Features

- **YOLOv11 Integration**: Leverages the latest YOLOv11 nano model (`yolo11n.pt`) for efficient real-time detection.
- **Advanced Data Augmentation**: 
    - Automated image mirroring and label synchronization.
    - Custom augmentation scripts for expanding training datasets.
- **Config-Driven**: Centralized configuration via `config.yaml` for managing paths, hyperparameters, and model settings.
- **Label Management**: Scripts to automatically adjust bounding box labels when images are transformed (e.g., mirrored).

## 📂 Project Structure

```text
├── train_final/            # Directory for training outputs and final models
├── main.py                 # Primary entry point for training or inference
├── config.yaml             # Configuration file for YOLO and datasets
├── serach_people.py        # Script for detecting and searching individuals in images
├── augumentation.py        # General data augmentation logic
├── augmenation_lables.py   # Corresponding label updates for augmented images
├── mirror_image.py         # Utility for horizontal/vertical image mirroring
├── mirrorr_label.py        # Utility to flip bounding box coordinates for mirrored images
└── yolo11n.pt              # Pre-trained YOLOv11 weights
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jjurzak/CrowdCounter.git
   cd CrowdCounter
   ```

2. **Install dependencies**:
   Ensure you have Python 3.8+ installed. You will need the `ultralytics` package and other standard CV libraries:
   ```bash
   pip install ultralytics opencv-python pyyaml numpy
   ```

## 💻 Usage

### 1. Data Augmentation
Before training, you can expand your dataset using the mirroring and augmentation scripts. This is particularly useful for crowd scenes to improve spatial invariance.
```bash
python mirror_image.py
python mirrorr_label.py
```

### 2. Training/Inference
Modify `config.yaml` to point to your local dataset paths, then run the main script:
```bash
python main.py
```

### 3. Detection
To run a specific search/count on a crowd image:
```bash
python serach_people.py --source path/to/your/image.jpg
```

## ⚙️ Configuration
The `config.yaml` file controls the behavior of the detection pipeline. You can specify:
- Training epochs and batch sizes.
- Image resolution.
- Path to training/validation datasets.

## 📄 License
[MIT License](LICENSE) (If applicable - check repository for specific license details)

## 👤 Author
Created by [jjurzak](https://github.com/jjurzak).
