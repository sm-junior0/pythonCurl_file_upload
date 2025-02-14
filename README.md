# Automated Image Upload Script

## Overview
This project is a Python script that monitors a folder for newly added images, uploads them to a specified server, and organizes the files after a successful upload to avoid redundancy.

## Features
- Monitors a folder where a camera regularly saves captured pictures.
- Automatically uploads each image after 30 seconds using the `curl` command.
- Moves successfully uploaded images to another folder (`uploaded`) for better organization.

## Requirements
- Python 3.6 or later
- Internet connection for uploading images

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/assignment_001.git
   cd assignment_001
   ```

2. Set up the required directories:
   - Replace the `monitor_folder` and `uploaded_folder` paths in the script with the appropriate directories on your system.

3. Verify that the upload URL in the script matches the provided endpoint:
   ```
   https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php
   ```

## Usage
1. Run the script:
   ```bash
   python upload_images.py
   ```

2. Add images to the monitoring folder. The script will:
   - Wait 30 seconds for each new image.
   - Upload the image using the `curl` command.
   - Move successfully uploaded images to the `uploaded` folder.

3. Monitor the terminal for upload status logs.

## Example `curl` Command
Here’s how the script uses the `curl` command to upload images:
```bash
curl -X POST -F imageFile=@/path/to/your/image.jpg https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php
```

## Troubleshooting
### Issue: Git `index.lock` error
1. Check and terminate any running Git processes:
   ```bash
   taskkill /IM git.exe /F
   ```
2. Delete the lock file:
   ```bash
   del .git\index.lock
   ```

### Issue: Monitoring folder path is incorrect or inaccessible
- Verify the folder path in the script and ensure the directory exists on your system.

## Folder Structure
```
assignment_001/
├── upload_images.py      # The Python script
├── README.md             # This file
└── .git/                 # Git folder (auto-generated)
```
