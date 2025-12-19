from ultralytics import YOLO  
import torch
import os

if __name__ == "__main__":
    torch.cuda.empty_cache()  
    model = YOLO("yolo11n.yaml") 

    results = model.train(data="config.yaml", epochs=1000, imgsz=1920, batch=4,) 



    