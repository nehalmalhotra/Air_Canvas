import cv2
import numpy as np

cap = cv2.VideoCapture(0)
canvas = None

# Define HSV ranges for Blue, Red, Green
color_ranges = {
    "blue": {
        "lower": np.array([100, 150, 0]),
        "upper": np.array([140, 255, 255]),
        "draw_color": (255, 0, 0)   # Blue in BGR
    },
    "red": {
        "lower1": np.array([0, 150, 120]),
        "upper1": np.array([10, 255, 255]),
        "lower2": np.array([170, 150, 120]),
        "upper2": np.array([180, 255, 255]),
        "draw_color": (0, 0, 255)   # Red in BGR
    },
    "green": {
        "lower": np.array([40, 70, 70]),
        "upper": np.array([80, 255, 255]),
        "draw_color": (0, 255, 0)   # Green in BGR
    }
}

last_points = { "blue": (0, 0), "red": (0, 0), "green": (0, 0) }

brush_size = 5
eraser_mode = False

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, data in color_ranges.items():
        mask = None
        if color_name == "red":
            mask1 = cv2.inRange(hsv, data["lower1"], data["upper1"])
            mask2 = cv2.inRange(hsv, data["lower2"], data["upper2"])
            mask = mask1 | mask2
        else:
            mask = cv2.inRange(hsv, data["lower"], data["upper"])

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > 1000:
            c = max(contours, key=cv2.contourArea)
            x2, y2, w, h = cv2.boundingRect(c)
            cv2.circle(frame, (x2, y2), 10, data["draw_color"], -1)

            x1, y1 = last_points[color_name]

            if x1 == 0 and y1 == 0:
                last_points[color_name] = (x2, y2)
            else:
                if eraser_mode:
                    canvas = cv2.line(canvas, (x1, y1), (x2, y2), (0, 0, 0), brush_size * 2)
                else:
                    canvas = cv2.line(canvas, (x1, y1), (x2, y2), data["draw_color"], brush_size)
                last_points[color_name] = (x2, y2)
        else:
            last_points[color_name] = (0, 0)

    frame = cv2.add(frame, canvas)

    # Display current mode & brush size
    cv2.putText(frame, f'Brush Size: {brush_size}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    mode = "Eraser ON" if eraser_mode else "Draw Mode"
    cv2.putText(frame, f'Mode: {mode}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, 'Press 1/2/3 to change brush size | E to toggle eraser | C to clear | S to save | Q to quit',
                (10, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Air Canvas", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('e'):
        eraser_mode = not eraser_mode
    elif key == ord('1'):
        brush_size = 5
    elif key == ord('2'):
        brush_size = 10
    elif key == ord('3'):
        brush_size = 20
    elif key == ord('s'):
        cv2.imwrite("air_canvas_output.png", canvas)
        print("Canvas saved as air_canvas_output.png")

cap.release()
cv2.destroyAllWindows()
