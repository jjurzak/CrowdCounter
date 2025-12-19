import os
from ultralytics import YOLO
import cv2

VIDEOS_DIR = os.path.join('vids')
video_path = os.path.join(VIDEOS_DIR, 'vid4.mp4')
video_path_out = '{}out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

frame = cv2.resize(frame, (1920, 1080))

H, W, _ = frame.shape

out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'runs', 'detect', 'train38', 'weights', 'best.pt')
model = YOLO(model_path)

threshold = 0.6 

cv2.namedWindow("Live Preview", cv2.WINDOW_NORMAL)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
color = (255, 255, 255)  
thickness = 4

frame_counter = 0  # Licznik klatek
frame_skip = 5     # Przeprowadzaj detekcję co 5 klatek

# Zmienna do przechowywania wyników detekcji
previous_detections = []

while ret:
    # Co 'frame_skip' klatek, uruchom detekcję
    if frame_counter % frame_skip == 0:
        results = model(frame, conf=threshold, iou=0.4, max_det=1000)[0]

        if results.boxes.data.shape[0] > 0: 
            previous_detections = []  # Zresetuj poprzednie wyniki detekcji
            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result
                if score > threshold:
                    previous_detections.append((x1, y1, x2, y2, score))

    # Narysuj wyniki detekcji na obecnej klatce
    for detection in previous_detections:
        x1, y1, x2, y2, score = detection
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

    text = f'Live people count: {len(previous_detections)}'
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = 10  
    text_y = 10 + text_size[1]
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness)

    resized_frame = cv2.resize(frame, (1920, 1080))

    out.write(frame)
    
    cv2.imshow("Live Preview", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = cap.read()
    frame_counter += 1  # Inkrementuj licznik klatek

cap.release()
out.release()
cv2.destroyAllWindows()
