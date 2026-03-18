import cv2
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

if len(sys.argv) > 2:
    logging.info(f'Only the first argument will be used as video path: {sys.argv[1]}')

paused = False 
button_area = None 
last_frame = None


def handle_click(event, x, y, flags, param):
    global paused, last_frame
    
    if event == cv2.EVENT_LBUTTONDOWN:
        btn_x, btn_y, btn_w, btn_h = button_area
        
        if btn_x <= x <= btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
            paused = not paused
            
            if last_frame is not None:
                draw_gui(last_frame)
                cv2.imshow('video', last_frame)


def on_trackbar(val):
    cap.set(cv2.CAP_PROP_POS_FRAMES, val)
    
    if paused:
        success, frame = cap.read()

        if success:
            global last_frame
            last_frame = frame
            draw_gui(frame)
            cv2.imshow('video', frame)


def draw_gui(img):
    global button_area
    
    btn_x, btn_y = 20, 20
    btn_w, btn_h = 100, 40
    button_area = (btn_x, btn_y, btn_w, btn_h)
    green = (0, 255, 0)
    red = (0, 0, 255)
    white = (255, 255, 255)
    
    if paused:
        color = green
        text = "PLAY"
    else:
        color = red
        text = "PAUSE"
        
    cv2.rectangle(img, 
                  (btn_x, btn_y), 
                  (btn_x + btn_w, btn_y + btn_h), 
                  color, 
                  -1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2
    
    (text_w, text_h), baseline = cv2.getTextSize(text, 
                                                 font, 
                                                 font_scale, 
                                                 thickness)
    text_x = btn_x + (btn_w - text_w) // 2
    text_y = btn_y + (btn_h + text_h) // 2
    
    cv2.putText(img, 
                text, 
                (text_x, text_y), 
                font, font_scale, 
                white, 
                thickness)
    


video_file = sys.argv[1]
cap = cv2.VideoCapture(video_file)
cv2.namedWindow('video')

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar('position', 'video' , 0, total_frames, on_trackbar)
cv2.setMouseCallback('video', handle_click)

while True:
    if not paused:
        success, frame = cap.read()

        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        last_frame = frame.copy()

        current_pos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        if current_pos > 0:
            cv2.setTrackbarPos('position', 'video', abs(current_pos))
            
        draw_gui(frame)
        cv2.imshow('video', frame)

    else:
        pass

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

