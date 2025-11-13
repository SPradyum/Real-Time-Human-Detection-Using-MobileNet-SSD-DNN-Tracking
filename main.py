import cv2
import time
import imutils
from ultralytics import YOLO

# Load YOLOv8 nano - auto-downloads on first run
model = YOLO("yolov8n.pt")

INPUT_WIDTH = 900

def detect_people(frame):
    results = model(frame, stream=True)

    detections = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            
            # class 0 = person
            if cls == 0 and conf > 0.35:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append((x1, y1, x2, y2, conf))
    return detections

def draw_boxes(frame, detections):
    for (x1, y1, x2, y2, conf) in detections:
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, f"{conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

def run_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("❌ Invalid video path!")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = imutils.resize(frame, width=INPUT_WIDTH)

        detections = detect_people(frame)
        draw_boxes(frame, detections)

        cv2.imshow("Video Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def run_camera():
    cap = cv2.VideoCapture(0)
    time.sleep(1)

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=INPUT_WIDTH)

        detections = detect_people(frame)
        draw_boxes(frame, detections)

        cv2.imshow("Camera Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def run_image(path):
    img = cv2.imread(path)
    if img is None:
        print("❌ Invalid image path!")
        return
    
    img = imutils.resize(img, width=INPUT_WIDTH)

    detections = detect_people(img)
    draw_boxes(img, detections)

    cv2.imshow("Image Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def menu():
    while True:
        print("\n=== Real-Time Human Detection Model ===")
        print("1. Camera")
        print("2. Video file")
        print("3. Image file")
        print("4. Exit")

        ch = input("Enter choice: ").strip()

        if ch == "1":
            run_camera()
        elif ch == "2":
            path = input("Video path: ")
            run_video(path)
        elif ch == "3":
            path = input("Image path: ")
            run_image(path)
        elif ch == "4":
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    menu()
