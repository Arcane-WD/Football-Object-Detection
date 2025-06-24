from ultralytics import YOLO
import torch

model = YOLO('models/best.pt')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Detected device: {device}")

if device == 'cuda':

    print("Running prediction on GPU (device=0)...")
    results = model.predict(r"Videos\08fd33_4.mp4", save=True, device=0, project="runs", name="test")

    print(results[0])
    print("==================================================================")
    for box in results[0].boxes:
        print(box)
