# Sound Control System Using Hand Gestures

About
This project demonstrates a system that controls sound volume based on hand gestures captured through the webcam. It utilizes OpenCV and MediaPipe to detect hand landmarks and translates hand movements into volume adjustments.

How to Run
Install Dependencies
Make sure you have the necessary dependencies installed. You can install them using pip:
pip install cv2 mediapipe numpy pycaw streamlit

Run the Application
Navigate to the project directory and run the Streamlit application:
cd path_to_project_directory
streamlit run project.py

Select App Mode
Upon running, you'll be presented with two options:

About App: Provides an overview of the application.
Run On Video: Allows you to use the webcam to control sound.
Using the Application

If you choose "Run On Video," the application will open your webcam. It will detect hand gestures, and based on the detected gestures, it will control the sound volume.

Recording Video
You can also record the video while using the application by checking the "Record Video" checkbox.

Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated.
