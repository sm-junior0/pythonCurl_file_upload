import os
import time
import subprocess
import shutil

WATCH_FOLDER = "C:\\Users\\user\\Pictures\\camera"  # Folder where the camera saves pictures
UPLOADED_FOLDER = "./uploaded"       # Folder to move uploaded pictures
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
UPLOAD_ATTRIBUTE = "imageFile"
CHECK_INTERVAL = 30
# Ensure the uploaded folder exists
os.makedirs(UPLOADED_FOLDER, exist_ok=True)
def upload_file(file_path):
    """Uploads a file using curl and returns whether the upload was successful."""
    try:
        result = subprocess.run(
            [
                "curl", "-X", "POST",
                "-F", f"{UPLOAD_ATTRIBUTE}=@{file_path}",
                UPLOAD_URL
            ],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
        return False
def monitor_and_upload():
    """Monitors the folder and uploads files at intervals."""
    print("Monitoring folder for new pictures...")
    while True:
        try:
            # List all files in the watch folder
            files = [f for f in os.listdir(WATCH_FOLDER) if os.path.isfile(os.path.join(WATCH_FOLDER, f))]
            for file_name in files:
                file_path = os.path.join(WATCH_FOLDER, file_name)
                print(f"Found file: {file_name}. Waiting {CHECK_INTERVAL} seconds before upload...")
                time.sleep(CHECK_INTERVAL)
                if upload_file(file_path):
                    print(f"Successfully uploaded: {file_name}")
                    # Move the file to the uploaded folder
                    shutil.move(file_path, os.path.join(UPLOADED_FOLDER, file_name))
                else:
                    print(f"Failed to upload: {file_name}. Retrying later...")
            # Wait before checking for new files again
            time.sleep(5)
        except Exception as e:
            print(f"Error during monitoring: {e}")
            time.sleep(5)
if __name__ == "__main__":
    monitor_and_upload()









