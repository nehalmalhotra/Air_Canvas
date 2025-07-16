#  Air Canvas

**Air Canvas** is a fun Computer Vision project built with **Python** and **OpenCV**. It lets you draw in the air by moving colored objects in front of your webcam — turning your camera feed into a virtual whiteboard!

---

##  Features

- Draw in real-time using a colored object (like a marker cap or colored tape).
- Supports multiple colors: **Blue**, **Red**, and **Green**.
- Toggle **Eraser Mode** to erase parts of your drawing.
- Change **brush size** while drawing.
- Clear the entire canvas instantly.
- Save your drawing as an image file.

---

##  How It Works

- Uses the **HSV color space** to detect colored objects.
- Tracks the object’s movement to draw lines on a virtual canvas.
- Overlays the virtual canvas on the live webcam feed.
- Lets you control the drawing with simple keyboard shortcuts.

---

##  Controls

| Key | Action |
|-----|--------|
| `1` | Small brush size |
| `2` | Medium brush size |
| `3` | Large brush size |
| `E` | Toggle eraser mode |
| `C` | Clear the canvas |
| `S` | Save the drawing (`air_canvas_output.png`) |
| `Q` | Quit the application |

---

##  How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/air-canvas.git
   cd air-canvas

2. **Install dependencies**
   ```bash
   pip install opencv-python numpy

3. **Run the Script**
   ```bash
   python air_can.py
   
##  Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

---

## Notes

- Make sure your webcam is connected and working.
- Use colored objects that match the defined HSV ranges in the script.
- Good lighting improves detection accuracy.
- Adjust HSV values if you want to detect different colors.

---

## License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share — just keep the original license notice!
