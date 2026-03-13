import os
import re
import subprocess
files = os.listdir("Videos")

for file in files:
    #print(f"## {file}")
    # Use regex to find "Tutorial <number>" pattern
    match = re.search(r'Tutorial\s*(\d+)', file)
    if match:
        tutorial_number = match.group(1)
    else:
        tutorial_number = "N/A"  # if no tutorial number found
    file_name=file.split("_")[0]
    print(tutorial_number,file_name)
    subprocess.run(["ffmpeg","-i",f"Videos/{file}",f"audios/{tutorial_number}_{file_name}.mp3"])