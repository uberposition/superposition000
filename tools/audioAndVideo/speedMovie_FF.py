import os
from pathlib import Path
import subprocess
from tqdm import tqdm


def speed_up_video_ffmpeg(input_path, output_path, speed_factor):
    command = (
        f"ffmpeg -i {input_path} -vf 'setpts={1/speed_factor}*PTS' -an {output_path}"
    )
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    home = str(Path.home())
    input_dir = os.path.join(home, "editVideo", "Input")
    output_dir = os.path.join(home, "editVideo", "Output")
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    speed_factor = float(input("Enter the speed-up factor (e.g., 1.5 or 2.0): "))

    video_files = [
        f for f in os.listdir(input_dir) if f.endswith((".mp4", ".avi", ".mov", ".mkv"))
    ]
    unique_videos = set(video_files)
    print(f"Unique videos to process: {len(unique_videos)}")

    for filename in tqdm(unique_videos, desc="Processing Videos"):
        input_path = os.path.join(input_dir, filename)
        output_filename = filename.split(".")[0] + f"_speed{speed_factor}x.mp4"
        output_path = os.path.join(output_dir, output_filename)
        speed_up_video_ffmpeg(input_path, output_path, speed_factor)

    print("The videos have quickened their pace, ready for your appraisal.")
