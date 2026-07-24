import os
import shutil
import time

while True:
    # 1. select DOWNLOADS folder
    folder = r"D:\Downloads"

    # 2. read all files inside the folder
    files = os.listdir(folder)

    # 3. create folders (if it didn't exist)
    images = os.path.join(folder, "Images")
    pdfs = os.path.join(folder, "PDF")
    mp3s = os.path.join(folder, "MP3")
    videos = os.path.join(folder, "Videos")
    archive = os.path.join(folder, "archive")
    others = os.path.join(folder, "Others")
    os.makedirs(images, exist_ok=True)
    os.makedirs(pdfs, exist_ok=True)
    os.makedirs(mp3s, exist_ok=True)
    os.makedirs(videos, exist_ok=True)
    os.makedirs(archive, exist_ok=True)
    os.makedirs(others, exist_ok=True)

    # 4. move files to their folders by type
    for file in files:
        file_lower = file.lower()
        src = os.path.join(folder, file)

        # Skip folders
        if not os.path.isfile(src):
            continue

        if file_lower.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            shutil.move(src, os.path.join(images, file))
        elif file_lower.endswith('.pdf'):
            shutil.move(src, os.path.join(pdfs, file))
        elif file_lower.endswith('.mp3'):
            shutil.move(src, os.path.join(mp3s, file))
        elif file_lower.endswith(('.mp4', '.mkv', '.mov', '.avi')):
            shutil.move(src, os.path.join(videos, file))
        elif file_lower.endswith(('.rar', '.zip', '.7z')):
            shutil.move(src, os.path.join(archive, file))
        else :
            shutil.move(src, os.path.join(others, file))
            
    time.sleep(30)   # check every 30 seconds
