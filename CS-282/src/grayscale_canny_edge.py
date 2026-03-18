
import cv2
import logging
import numpy as np
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    logging.error("Could not open webcam")
else:
    logging.info("Webcam opened. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            logging.error("Failed to grab frame")
            break
        
        height, width = frame.shape[:2]
        canvas = np.zeros((height, width * 3, 3), dtype=np.uint8)
        
        # Stage 1: Original frame
        canvas[:, 0:width] = frame
        
        # Stage 2: Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) 
        canvas[:, width:width*2] = gray_bgr
        
        # Stage 3: Canny edge detection
        edges = cv2.Canny(gray, 50, 150)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        canvas[:, width*2:width*3] = edges_bgr
        
        # Add labels
        cv2.putText(canvas, 
                    'Original', 
                    (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 255, 0), 
                    2)
        cv2.putText(canvas, 
                    'Grayscale', 
                    (width + 10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 255, 0), 
                    2)
        cv2.putText(canvas, 
                    'Canny Edges', 
                    (width*2 + 10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 255, 0), 
                    2)
        
        cv2.imshow('Webcam Processing Pipeline', canvas)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    logging.info("Webcam closed.")