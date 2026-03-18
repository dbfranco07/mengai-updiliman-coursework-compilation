
import cv2
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

if len(sys.argv) > 2:
    logging.info(f'Only the first argument will be used as image path: {sys.argv[1]}')

def mouse_callback(event, x, y, flags, param):
    img = param['img']
    display_img = param['display_img']
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get BGR values at the clicked location
        b, g, r = img[y, x]
        
        # Create a copy for displaying text
        param['display_img'] = img.copy()
        
        # Display coordinates and BGR values as text on image
        text = f"({x}, {y}): B={b}, G={g}, R={r}"
        cv2.putText(
            img=param['display_img'], 
            text=text, 
            org=(x + 10, y - 10),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale=0.5, 
            color=(0, 255, 0), 
            thickness=2
        )
        cv2.circle(
            img=param['display_img'], 
            center=(x, y), 
            radius=2, 
            color=(0, 255, 0), 
            thickness=-1)
        
        cv2.imshow(
            winname='Image - Click to see pixel values', 
            mat=param['display_img']
        )
        
        # Also print to console
        logging.info(f"Coordinates: ({x}, {y}), BGR: ({b}, {g}, {r})")

# Load an image
img_path = sys.argv[1]
logging.info(f"Loading image from: {img_path}")
img = cv2.imread(img_path)

if img is None:
    logging.error(f"Could not load image from {img_path}")
else:
    # Create a copy for display
    display_img = img.copy()
    
    # Create window and set mouse callback
    cv2.namedWindow('Image - Click to see pixel values')
    param = {'img': img, 'display_img': display_img}
    cv2.setMouseCallback(
        window_name='Image - Click to see pixel values', 
        on_mouse=mouse_callback, 
        param=param
    )
    
    # Display image
    cv2.imshow(
        winname='Image - Click to see pixel values', 
        mat=display_img
    )
    
    logging.info("Click on the image to see coordinates and pixel values. Press any key to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()