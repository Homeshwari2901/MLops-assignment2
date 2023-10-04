# MLops-assignment2
Person Re-Identification Using CCTV Footage

The framework used to accomplish this task relies on MOT and ReID to track and re-identify ID's of humans, respectively. The tracking can be completed using YOLO_v3 or YOLO_v4 and ReID relies on KaiyangZhou's Torchreid library.

Step 1: Data Collection and Preprocessing

Collected a dataset of publicly available CCTV footage that includes multiple camera views capturing people walking.
Preprocessed the video data into a format suitable for model training. Firstly install various libraries from python such as numpy,torch,keras etc

Step 2: Person Detection and Tracking:
Implemented a person detection using a YOLO model
Developed a tracking algorithm to track individuals across frames and camera views.

And then in Step 3: We have done the feature extraction from the CCtv Footage using an extration methods.

Step 4: Person Re-Identification Model 1.Firstly we need to design and implement a person re-identification model using Pytorch which is used for an open source machine learning (ML) framework based on the Python programming language and the Torch library. Torch is an open source ML library used for creating deep neural networks and is written in the Lua scripting language. And then we ned to train the model on your dataset, using the extracted features. 2. Evaluate the model's performance on person re-identification tasks.

Step 5: Visualization and Demonstration For Visualization we can see that if a person is coming twice but he willbe counted as one only and that show the effectiveness of your person re-identification model. There are 2 videos such as Single1.mp4 and Double1.mp4 so we can demonstrate on both the CCTV Footage and check it.
