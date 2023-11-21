import os
from pathlib import Path
import subprocess
from tqdm import tqdm

# Define the paths based on user's home directory
home = str(Path.home())
input_dir = os.path.join(home, "editVideo", "Input")
output_dir = os.path.join(home, "editVideo", "Output")

# Check and create directories if they don't exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


def convert_videos(input_dir, output_dir):
    video_files = [
        f for f in os.listdir(input_dir) if f.endswith((".mp4", ".avi", ".mov", ".mkv"))
    ]  # Add more formats if needed
    unique_videos = set(video_files)
    print(f"Unique videos to process: {len(unique_videos)}")

    for filename in tqdm(unique_videos, desc="Processing Videos"):
        input_path = os.path.join(input_dir, filename)
        output_filename = filename.split(".")[0] + "_FFResize.mp4"
        output_path = os.path.join(output_dir, output_filename)

        # Use FFmpeg to resize the video
        command = f"ffmpeg -i {input_path} -vcodec libx264 -crf 24 -pix_fmt yuv420p -profile:v high -level 4.0 {output_path}"
        subprocess.run(command, shell=True)


# Call the function to convert videos
convert_videos(input_dir, output_dir)
