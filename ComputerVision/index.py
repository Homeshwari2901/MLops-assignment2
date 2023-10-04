import cv2
import os

# Step 1: Collecting CCTV Footage
# You should replace 'sample_video.mp4' with your actual video file or data collection source.

video_path = 'sample_video.mp4'

# Step 2: Preprocessing Video Data
# Create a directory to store extracted frames and annotations
output_dir = 'dataset_frames'
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame (e.g., resize, normalize)
    # You can apply additional preprocessing steps here as needed

    # Save the frame
    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

# Close the video file
cap.release()

# Print the number of frames processed
print(f"Total frames extracted: {frame_count}")

# Optionally, you can annotate bounding boxes and store metadata here.

# Step 3: Data Organization
# After preprocessing, your 'output_dir' will contain the frames suitable for model training.

# Example directory structure:
# - dataset_frames/
#   - frame_0000.jpg
#   - frame_0001.jpg
#   - ...
