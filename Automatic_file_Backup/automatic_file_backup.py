import os
import shutil      #for copying content
import datetime
import schedule     #for scheduling 
import time

SOURCE_DIR = "ENTER YOUR SOURCE DIRECTORY"
DESTINATION_DIR = "ENTER YOUR DESTINATION DIRECTORY"


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    #dest_dir has dest_path/today_date as folder name

    try:
        shutil.copytree(source, dest_dir)           #recursively copies files and paste there in dest_dir 
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("18:57").do(
    lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR))

while True:
    schedule.run_pending()
    time.sleep(60)