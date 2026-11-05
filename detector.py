
import cv2
from collections import Counter
from ultralytics import YOLOWorld
from classes import ALL_CLASSES


class ObjectDetector:

    def __init__(self, model_path="yolov8s-worldv2.pt", confidence=0.25):

        print("Loading YOLO-World model...")

        self.model = YOLOWorld(model_path)

        # Remove duplicate prompts
        self.classes = list(dict.fromkeys(ALL_CLASSES))

        # Set custom object vocabulary
        self.model.set_classes(self.classes)

        self.confidence = confidence

        print("YOLO-World loaded successfully!")
        print("Unique object prompts:", len(self.classes))

    def detect(self, frame):

        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            imgsz=640,
            verbose=False
        )

        output_frame = frame.copy()
        object_counts = Counter()
        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])
                class_name = self.classes[class_id]
                confidence = float(box.conf[0])

                x1, y1, x2, y2 = map(
                    int, box.xyxy[0].tolist()
                )

                cv2.rectangle(
                    output_frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                label = f"{class_name} {confidence:.2f}"

                cv2.putText(
                    output_frame,
                    label,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

                object_counts[class_name] += 1

                detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 3),
                    "box": [x1, y1, x2, y2]
                })

        return output_frame, object_counts, detections
