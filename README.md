
# Real-time-Face-Recognition-and-Attendance-System

Face Recognition and Attendance System This project demonstrates a face recognition system that uses a webcam to capture images, detects faces, and recognizes individuals using a K-Nearest Neighbors (KNN) classifier. The system also logs attendance with a timestamp into a CSV file.

## Setup Instructions
Install Dependencies:

`OpenCV: pip install opencv-python
Scikit-learn: pip install scikit-learn
pywin32: pip install pywin32`

Prepare Data Directory:

Create a directory named data and place the Haarcascade XML file`(haarcascade_frontalface_default.xml)`in it.

## Run Face Data Collection:

Execute the first script to capture and save face data.

Train and Test Face Recognition:
Ensure the bgimage.png is in the same directory as the scripts.

Run the second script to start face recognition and attendance logging.

Check Attendance Logs:
Attendance logs are saved in the Attendance directory as `CSV files`.

This project is a practical demonstration of integrating face recognition with attendance logging, suitable for environments such as classrooms or workplaces.
## Face Data Collection Script Description: 
This script captures face images from a webcam, processes them, and stores them in a dataset for later use in training a face recognition model. It uses OpenCV for image capture and face detection, and the collected face data is saved using Python's pickle module.
## 2. Face Recognition and Attendance Logging Script
Description:

This script uses a pre-trained `KNN classifier` to recognize faces captured from a webcam in real-time. It detects faces, recognizes individuals, and logs their attendance with a timestamp into a CSV file. The system also provides audio feedback when attendance is recorded.

Key Features:

Loads pre-trained face recognition model and labels.

Captures and processes real-time video feed from a webcam.

Detects faces and recognizes individuals using KNN.

Logs attendance with timestamps into CSV files.

Provides audio feedback using the pywin32 library.


## Screenshots


## Screenshots

![App Screenshot](https://github.com/manishsinghaj/Real-time-Face-Recognition-and-Attendance-System/blob/main/bf092e36-c0b8-4b3e-9535-f91ef4153f41.jpg?raw=true)

