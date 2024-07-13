# Real-time-Face-Recognition-and-Attendance-System
Face Recognition and Attendance System This project demonstrates a face recognition system that uses a webcam to capture images, detects faces, and recognizes individuals using a K-Nearest Neighbors (KNN) classifier. The system also logs attendance with a timestamp into a CSV file. 

#Face Data Collection Script
Description:
This script captures face images from a webcam, processes them, and stores them in a dataset for later use in training a face recognition model. It uses OpenCV for image capture and face detection, and the collected face data is saved using Python's pickle module.

Key Features:

Initializes webcam and face detection model.
Captures images and detects faces in real-time.
Resizes detected face images to a consistent size.
Stores face images and corresponding labels.
Saves collected data into serialized files (.pkl format) for future use.

import these libraries:
import cv2
import pickle
import numpy as np
import os
