# Face Detection in Videos README

This script detects faces in videos using OpenCV's Haar Cascade Classifier and saves the frames containing detected faces in separate folders.

## Usage

1. Update the `video_directory` variable to point to the directory containing the input videos.
2. Update the `output_directory` variable to specify the directory where the output frames will be saved.
3. Run the script.

## Description

- The script iterates through each video file in the specified directory.
- For each video file, it opens the video and reads each frame.
- It converts each frame to grayscale and applies the Haar Cascade classifier to detect faces.
- If a face is detected, it draws a rectangle around the face and calculates a Region of Interest (ROI) around it.
- It saves the frames containing detected faces in separate folders within the output directory.

## Example

Suppose we have video files in the directory `videos` and want to save the frames containing detected faces in the directory `located`. After running the script, the output directory structure will look like this:

