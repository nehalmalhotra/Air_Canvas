# Air_Canvas
Air Canvas is a fun Computer Vision project built using OpenCV and Python. It lets you draw in the air using colored objects (like a marker cap or colored tape) tracked by your webcam — turning your camera feed into a virtual drawing canvas!

Features
Draw in real-time by moving a colored object in front of your webcam.

Supports multiple colors: Blue, Red, and Green.

Toggle Eraser Mode to erase parts of your drawing.

Adjust brush size on the fly.

Clear the canvas with a single key press.

Save your masterpiece as an image file.

How It Works
Uses HSV color space to detect colored objects.

Tracks the movement of the object to draw lines on a virtual canvas.

Merges the virtual canvas with the live webcam feed for display.

Supports basic keyboard controls for an interactive experience.

Controls
Key	Action
1	Set brush size to small
2	Set brush size to medium
3	Set brush size to large
E	Toggle eraser mode
C	Clear the canvas
S	Save the drawing (air_canvas_output.png)
Q	Quit the application

How to Run
Clone this repository

bash
Copy
Edit
git clone https://github.com/yourusername/air-canvas.git
cd air-canvas
Install requirements

bash
Copy
Edit
pip install opencv-python numpy
Run the script

bash
Copy
Edit
python air_can.py

Requirements
Python 3.x

OpenCV (opencv-python)

NumPy

Notes
Make sure your webcam is connected and working.

Use colored objects that match the predefined HSV ranges (or tweak them in the script).

Works best in good lighting conditions for accurate color detection.

Example
Draw with your hands in the air and see your creation appear live!

Credits
Made with ❤️ using OpenCV and Python.

License
This project is open-source under the MIT License.

